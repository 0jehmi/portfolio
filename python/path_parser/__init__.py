"""
지정한 패턴의 템플릿을 생성하고 패턴과 선택한 경로를 매칭시켜서 원하는 경로 값을 추출합니다.

how to use


ps = PathSearch()
# 클래스를 불러옵니다.

self._json_path = "json저장경로/lucidity.json"
# init의 self._json_path에 json파일을 저장할 경로를 입력합니다.

ps.add_temp('이름','/패턴경로/{추출하고 싶은 값}')
# 원하는 템플릿 이름과 패턴을 추가해줍니다.

ps.set_temp_name = '이름'
# 추가한 템플릿 이름 중 원하는 템플릿 이름을 입력합니다.

print(ps.set_path('/파일경로'))
# 추출하고 싶은 파일의 경로를 적어줍니다.

"""

from path_parser.path_parse import PathParse
