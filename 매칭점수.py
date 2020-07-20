def solution(word, pages):
    page_dict = [{
                'page_idx': i,
                'page_url': '',
                'basic_score' : 0,
                'link_from_other_page': [],
                'external_link_cnt': 0,
                'link_score': 0,
                'matching_score': 0,
            } for i in range(len(pages))]

    def get_page_url(page):
        start_idx = page.find('<meta property="og:url')
        end_idx = page.find('"/>', start_idx)
        return page[start_idx + 33: end_idx]

    def get_basic_score(word, page):
        cnt = 0
        splited_page = page.replace('\n', ' ').split(' ')
        for p in splited_page:
            if p.lower() == word.lower():
                cnt += 1

        return cnt

    def get_external_cnt(page_idx, page, page_url):
        cnt = 0
        idx = 0
        while True:
            a_link_idx = page.find('<a href="', idx)
            # 해당 페이지에 a링크가 없을 경우
            if a_link_idx == -1:
                return cnt
            
            end_idx = page.find('">', a_link_idx)
            link_url = page[a_link_idx + 9:end_idx]
            idx = end_idx + 1

            for page_info in page_dict:
                if page_info['page_url'] == link_url:
                    page_info['link_from_other_page'].append(page_idx)
                    break
            
            cnt += 1

    def get_link_score(page_info):
        score = 0
        for page_idx in page_info['link_from_other_page']:
            linked_page_info = page_dict[page_idx]
            if linked_page_info['external_link_cnt']:
                score += linked_page_info['basic_score'] / linked_page_info['external_link_cnt']
        return score

    for idx, page in enumerate(pages):
        page_url = get_page_url(page)
        page_info = page_dict[idx]
        page_info['page_url'] = page_url
        page_info['basic_score'] = get_basic_score(word, page)
    
    for idx, page in enumerate(pages):
        page_info = page_dict[idx]
        page_info['external_link_cnt'] = get_external_cnt(idx, page, page_url)
        
    for page_info in page_dict:
        page_info['link_score'] = get_link_score(page_info)
        page_info['matching_score'] = page_info['basic_score'] + page_info['link_score']

    return sorted(page_dict, key=lambda  x: -x['matching_score'])[0]['page_idx']


word = 'blind'
pages  = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word, pages))
