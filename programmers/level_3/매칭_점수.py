def solution(word, pages):
    def search_word(word, body, type):
        cnt = 0
        idx = 0
        idx_list = []
        n = len(word)
        m = len(body)
        while idx < m - n:
            if body[idx].lower() == word[0].lower():
                start = idx
                is_target = False
                for i in range(1, n):
                    idx += 1
                    if body[idx].lower() == word[i].lower():
                        is_target = True
                    else:
                        is_target = False
                        break
                char = body[idx+1].lower()
                
                if is_target == True and (ord(char) < 97 or ord(char) > 122):
                    if type == "cnt":
                        if start != 0:
                            temp = ord(body[start-1].lower())
                            if temp >= 97 and temp <= 122:
                                continue
                        cnt += 1
                    else:
                        idx_list.append(idx)
            else:
                idx+=1
        return cnt if type == "cnt" else idx_list
    
    p = len(pages)
    score = [0] * p
    basic_score = [0] * p
    link_score = [0] * p
    total = [0] * p
    link_page = [None] * p
    external_link = [[] for _ in range(p)]
    
    for idx, page in enumerate(pages):
        # i = 135
        # while True:
        #     i+=1
        #     if page[i] == '\"':
        #         if page[i+1] == "/" and page[i+2] == ">":
        #             link_page[idx] = page[135:i]
        #         else:
        #             link_page[idx] = "x"
        #         break
        # print(link_page)
        # # link_page[idx] = page[135:i]
        
        # 페이지의 body 부분 추출
        body_start = search_word("<body>", page, idx)[0]
        body_end = search_word("</body>", page, idx)[0]
        body = page[body_start+1:body_end-6]
        
        # 현재 페이지의 주소값 저장
        start = search_word('<meta property="og:url" content=', page, idx)[0] + 1
        k = start
        flag = False
        while k < body_start:
            k+=1
            if page[k:k+2] == "/>":
                flag= True
                break
        if flag == True:
            link_page[idx] = page[start+1:k-1]
        else:
            link_page[idx] = 'x'

        # 기본 점수
        cnt = search_word(word, body, "cnt")
        basic_score[idx] += cnt
        total[idx] += cnt
        # 링크 수 
        ex_links = search_word('<a href="https:', body, "idx")
        link_score[idx] += len(ex_links)
        # 외부 링크 
        for ex_link in ex_links:
            start = ex_link-5
            i = start
            while True:
                i += 1
                if body[i] == '>':
                    break
            external_link[idx].append(body[start:i-1])
    for i in range(p):
        link = link_page[i]
        for j in range(p):
            if i != j and link in external_link[j]:
                total[i] += basic_score[j] / link_score[j]
    max_v = max(total)
    for i in range(p):
        if total[i] == max_v:
            return i