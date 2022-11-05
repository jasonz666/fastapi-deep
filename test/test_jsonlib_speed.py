# coding:utf-8
__author__ = r'Jason<jasonz666@qq.com>'

# test some json libs and serialization

import json
import orjson
import msgpack
import typing
import time


def test_dumps(
        lib: typing.Union[json, orjson, msgpack],
        d: dict,
        loop=1000,
        count=300
) -> float:
    total = []

    for lp in range(loop):
        for ct in range(count):
            start = time.perf_counter_ns()
            lib.dumps(d)
            end = time.perf_counter_ns()
            total.append(end - start)

    return sum(total) / len(total)


def test_loads(
        lib: typing.Union[json, orjson, msgpack],
        d: typing.Union[str, bytes],
        loop=1000,
        count=300
) -> float:
    total = []

    for lp in range(loop):
        for ct in range(count):
            start = time.perf_counter_ns()
            lib.loads(d)
            end = time.perf_counter_ns()
            total.append(end - start)

    return sum(total) / len(total)


if __name__ == '__main__':

    """
    结论：
        追求速度，使用 orjson
        追求更小的序列化size，使用 msgpack

    序列化、反序列化：
        orjson最快 win
        msgpack较快
        json最慢

    序列化大小：
        msgpack更小(序列化成二进制数据) win
    """

    data = {
        'name': ['Tom', 'Jerry'],
        'age': 20,
        'from': 'somewhere',
        'tupple': (1, 2, 3)
    }

    data_str = b'{"name":"xxxx"}'
    data_bin = b'\x84\xa4name\x92\xa3Tom\xa5Jerry\xa3age\x14\xa4from\xa9somewhere\xa6tupple\x93\x01\x02\x03'

    print('json dumps len:', len(orjson.dumps(data)))
    print('msgpack dumps len:', len(data_bin))
    print()

    print('json dumps'.center(60, '='))
    print(f'nano second, ret={(ret:=test_dumps(json, data))}')
    print(f'micro second, {ret/1000=}')
    print(f'million second, {ret/1000000=}')

    print()
    print('orjson dumps'.center(60, '='))
    print(f'nano second, ret={(ret:=test_dumps(orjson, data))}')
    print(f'micro second, {ret/1000=}')
    print(f'million second, {ret/1000000=}')

    print()
    print('msgpack dumps'.center(60, '='))
    print(f'nano second, ret={(ret:=test_dumps(msgpack, data))}')
    print(f'micro second, {ret/1000=}')
    print(f'million second, {ret/1000000=}')

    print()
    print('+' * 60)
    print()

    print('json loads'.center(60, '='))
    print(f'nano second, ret={(ret:=test_loads(json, data_str))}')
    print(f'micro second, {ret/1000=}')
    print(f'million second, {ret/1000000=}')

    print()
    print('orjson loads'.center(60, '='))
    print(f'nano second, ret={(ret:=test_loads(orjson, data_str))}')
    print(f'micro second, {ret/1000=}')
    print(f'million second, {ret/1000000=}')

    print()
    print('msgpack loads'.center(60, '='))
    print(f'nano second, ret={(ret:=test_loads(msgpack, data_bin))}')
    print(f'micro second, {ret/1000=}')
    print(f'million second, {ret/1000000=}')
