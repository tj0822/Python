#-*- coding:utf-8 -*-


# str이나 bytes를 입력으로 받고 str을 반환하는 메서드
def to_str(bytes_or_str):
	if isinstance(bytes_or_str, bytes):
		value = bytes_or_str.decode('utf-8')
	else:
		value = bytes_or_str
	return value    # str 인스턴스

# str이나 bytes를 입력받고 bytes를 반환하는 메서드
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

