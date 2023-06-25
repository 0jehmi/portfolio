import os.path
import lucidity
import json


class PathParse:

    def __init__(self):
        """

        __init__ 메서드는 초기화 메서드로 class Path_Search:에서 사용 될 객체의 성질을 정해줍니다.

        """
        self._templates = {}
        self._template = None
        self._path = ""
        self._data = None
        self._json_path = "/lucidity.json"
        self.load_temp()
        self._set_temp_name = None
        self._set_path_data = None

    def add_temp(self, nick, pattern):
        """

        *_templates*에 새로운 template을 추가하고 json파일에 저장합니다.

        Args:
            nick (str): dictionary of keys
            pattern (str): dictionary of value

        """
        self._templates[nick] = pattern
        self.save_temp()

    def save_temp(self):
        """

        *_json_path*경로에 저장된 json파일을 쓰기모드로 읽어오고 *_templates*의 내용을 json파일에 저장합니다.

        """
        with open(self._json_path, "w") as json_file:
            json.dump(self._templates, json_file)

    def load_temp(self):
        """

        *_json_path*경로에 파일이 존재하면 True를 반환하고 json파일을 읽기모드로 읽어와서 *_templates*에 할당해줍니다.

        """
        if os.path.exists(self._json_path):
            with open(self._json_path, "r") as json_file:
                self._templates = json.load(json_file)

    @property
    def set_temp_name(self):
        """

        Returns: *_set_temp_name*

        """
        return self._set_temp_name

    @set_temp_name.setter
    def set_temp_name(self, value):
        """

        같은 클래스에 포함된 _set_temp 메서드를 실행하고
        저장된 템플릿 이름과 일치하지 않는 이름을 입력하면 나오는 오류문을 실행합니다.

        Args:
            value (str): 사용자가 지정한 템플릿 이름입니다. 이것은 lucidity 탬플릿에 저장된 템플릿 이름과
            매칭시켜서 dictionary keys값으로 나옵니다.

        """
        if value not in self._templates:
            raise ValueError("Error: 존재하지 않는 템플릿 이름입니다. 다시 입력하세요.")
        self._set_temp_name = value
        self._set_temp(value)

    def _set_temp(self, key):
        """

        *_templates*의 값을 전달받은 아규먼트 *key*와 i가 같을 때 *temp*에 값을 할당하고
        lucidity.Template에 *key*와 *temp*를 인수로 전달하여 생성한 템플릿을 *_template*에 할당합니다.

        Args:
            key (str): *_templates* of keys

        """
        temp = ""
        for i in self._templates:
            if i == key:
                temp = self._templates[i]
        self._template = lucidity.Template(key, temp)

    @property
    def set_path_data(self):
        """

        Returns: *set_path_data*

        """
        return self.set_path_data

    @set_path_data.setter
    def set_path_data(self, value):
        """

        같은 클래스에 포함된 set_path 메서드를 실행하고
        저장된 템플릿 형식과 일치하지 않는 경로를 입력하면 나오는 오류문을 실행합니다.

        Args:
            value (str): 사용자가 지정하는 파일 경로입니다. 이것은 lucidity 탬플릿에 저장된 템플릿 경로와
            매칭시켜서 dictionary value값으로 나옵니다.

        """
        if value not in self._path:
            raise ValueError("Error: 경로가 템플릿 형식과 일치하지 않습니다. 다시 입력하세요.")
        self._set_path_data = value
        self.set_path(value)

    def set_path(self, path):
        """

        *_template*에 들어있는 데이터를 추출하고 *_path*의 데이터와 비교하여 결과 값을 추출합니다.

        Args:
            path (str): *_path*에 저장된 경로 데이터를 가져옵니다.

        Returns: 결과 값 *_date*를 반환합니다.

        """
        self._path = path
        self._data = self._template.parse(path)
        return self._data


def main():
    pps = PathParse()


if __name__ == "__main__":
    main()
