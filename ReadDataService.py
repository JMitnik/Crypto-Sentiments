import csv

def read_data(source, file_name):
    result = []
    with open('data/'+source+'/'+ file_name, encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            result.append({
                'date': row[0],
                'content': row[1],
                'source': row[2]
            })

    return result


print(read_data('sm', 'bitcoin-tweets.csv'))
