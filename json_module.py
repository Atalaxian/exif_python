import json


class JSON:

    @staticmethod
    def from_json_bytes_to_dict(data: bytes) -> dict:
        result_dict = json.loads(data)
        return result_dict

    @staticmethod
    def from_dict_to_json_byte(data: dict) -> bytes:
        json_result = json.dumps(data)
        bytes_from_json = json_result.encode('UTF-8')
        return bytes_from_json
