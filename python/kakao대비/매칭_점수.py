import re

def solution(word, pages):
    N = len(pages)
    page_infos = [{
        'idx': 0,
        'page_link': '',      # 해당 페이지의 링크
        'ex_link_cnt': 0,     # 해당 페이지의 외부 링크 수
        'basic_score': 0,     # 기본점수 (검색어 등장 횟수)
        'link_score': 0,      # 링크점수 sum(이 페이지로의 링크를 가진 페이지의 기본점수 / 외부링크수)
        'matching_score': 0   # 매칭점수 (기본점수 + 링크점수)
    } for _ in range(N)]

    link_to_page = {}
    link_from_page = {}

    def get_page_link(html_str):
        result = re.findall(r'<meta property="og:url" content=[\'"]?([^\'" >]+)', html_str)
        return result[0]
    
    def get_basic_score(word, html_str):
        html_str = html_str.upper()
        N = len(word)
        cnt = 0
        for i in range(len(html_str) - N):
            if html_str[i:i+N] == word.upper() and not html_str[i+N].isalpha() and (i > 0 and not html_str[i-1].isalpha()):
                cnt += 1
        return cnt

    def get_ex_links(html_str):
        return re.findall(r'<a href=[\'"]?([^\'" >]+)', html_str)
    
    for idx, page in enumerate(pages):
        page_info = page_infos[idx]
        page_info['idx'] = idx
        page_link = get_page_link(page)
        page_info['page_link'] = page_link
        link_to_page[page_link] = idx

        ex_links = get_ex_links(page)
        page_info['ex_link_cnt']= len(ex_links)
        for ex_link in ex_links:
            if ex_link in link_from_page:
                link_from_page[ex_link].append(idx)
            else:
                link_from_page[ex_link] = [idx]
        
        basic_score = get_basic_score(word, page)
        page_info['basic_score'] = basic_score

    def calc_link_score(arr):
        result = 0
        for idx in arr:
            page_info = page_infos[idx]
            result += page_info['basic_score'] / page_info['ex_link_cnt']
        return result

    for link in link_from_page:
        if link not in link_to_page:
            continue
        page_idx = link_to_page[link]
        page_info = page_infos[page_idx]
        page_info['link_score'] = calc_link_score(link_from_page[link])
    
    for page_info in page_infos:
        page_info['matching_score'] = page_info['link_score'] + page_info['basic_score']

    page_infos.sort(key=lambda x: (-x['matching_score'], x['idx']))
    return page_infos[0]['idx']

word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word, pages))