import asyncio

data = {}


def split_csv_line(line: str):
    basic = [token.strip() for token in line.split()]
    final = []

    i = 0
    start_i = None
    is_inside_str = False
    while i < len(basic):
        if is_inside_str:
            basic[start_i] += basic[i + 1]
            if basic[i][-1] == '"':
                is_inside_str = False
        else:
            final.append(basic[i])
            if basic[i][0] == '"':
                is_inside_str = True
                start_i = i
        i += 1
    return tuple(final)


async def read_csv():
    global data
    with open('./data.csv', 'r') as f:
        data['header'] = f.readline().split(',')
        data['data'] = []
        while line := f.readline():
            data['data'].append(split_csv_line(line))
            print('>>>', data)
            await asyncio.sleep(0.1)
    return data


def convert_to_dict(data: tuple[str], header: tuple[str]):
    return {
        header[i]: data[i]
        for i in range(len(data))
    }


async def parse_csv_lines_to_dict():
    global data

    while True:
        for i, line in enumerate(reversed(data['data'])):
            if isinstance(line, tuple):
                data['data'][i] = convert_to_dict(data['data'][i], data['header'])
            else:
                break
        print('<<<', data)
        await asyncio.sleep(0.1)


async def main():
    csv_task = asyncio.create_task(read_csv())
    csv_conversion_task = asyncio.create_task(parse_csv_lines_to_dict())

    # run multiple parallel tasks:

    while True:
        print(data)
        # TODO use the current data:
        await asyncio.sleep(0.05)
        if csv_task.done() and csv_conversion_task.done():
            break


if __name__ == "__main__":
    asyncio.run(main())

    print('here')
