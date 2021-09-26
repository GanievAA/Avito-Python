import csv


def read_csv(file_path: str, delimiter: str):
    """Opens and reads csv file"""
    csv_file = open(file_path, encoding="utf-8")
    csv_reader = csv.reader(csv_file, delimiter=delimiter)
    return csv_reader


def show_dep_hierarchy(opened_file_with_csv_data) -> dict:
    """Shows all divisions in each department.
    Example:
        csv_file = open('some_file.csv', encoding="utf-8")
        opened_file_with_csv_data = csv.reader(csv_file, delimiter=delimiter)
        results = show_dep_hierarchy(opened_file_with_csv_data)
        print(results)
    """
    departament_dict = dict()
    for ind, row in enumerate(opened_file_with_csv_data):
        if ind != 0:
            if row[1] not in departament_dict:
                departament_dict[row[1]] = {row[2]}
            elif row[1] in departament_dict:
                current_divisions = departament_dict[row[1]]
                current_divisions.add(row[2])
                departament_dict[row[1]] = current_divisions
    return departament_dict


def show_dep_report(opened_file_with_csv_data) -> dict:
    """The function returns statistics about number of employees,
    min, average and max salary in each department"""
    departament_dict = dict()
    for ind, row in enumerate(opened_file_with_csv_data):
        if ind != 0:
            if row[1] not in departament_dict:
                wage = row[-1]
                salaries = [wage]
                num_emp = 1
                departament_dict[row[1]] = {'num employees': num_emp,
                                            'min salary': float(wage),
                                            'avg salary': float(wage) / num_emp,
                                            'max salary': float(wage),
                                            'all salaries': salaries
                                            }
            elif row[1] in departament_dict:
                salaries = departament_dict[row[1]]['all salaries']
                salaries.append(row[-1])
                cur_num_emp = departament_dict[row[1]]['num employees'] + 1
                departament_dict[row[1]] = {'num employees': cur_num_emp,
                                            'min salary': min(list(map(float, salaries))),
                                            'avg salary': round(sum(list(map(float, salaries))) / cur_num_emp, 1),
                                            'max salary': max(list(map(float, salaries))),
                                            'all salaries': salaries
                                            }
    for key in departament_dict.keys():
        del departament_dict[key]['all salaries']
    return departament_dict


def save_results_into_csv(file_name) -> csv:
    """Saves results of the function show_dep_report(opened_file_with_csv_data) into csv file"""
    saved_file = open(file_name, 'w')
    csv_red = read_csv(file_path=r'C:\Users\Abdurakhim\Desktop\Corp_Summary.csv', delimiter=';')
    results = show_dep_report(csv_red)
    writer = csv.writer(saved_file)
    for key, value in results.items():
        writer.writerow([key, value])
    saved_file.close()


if __name__ == '__main__':
    print('Нажмите 1, если хотите вывести иерархию комманд компании')
    print('Нажмите 2, если хотите вывести результаты своднного отчета по департаментам')
    print('Нажмите 3, если хотите сразу сохранить результаты сводного отчета')
    command = input("Выбирите действие: ")
    while command not in ['1', '2', '3']:
        print('Выбирите пожалуйста 1, 2 или 3')
        command = input("Выбирите действие: ")
    if command == '1':
        csv_read = read_csv(file_path=r'C:\Users\Abdurakhim\Desktop\Corp_Summary.csv', delimiter=';')
        print(show_dep_hierarchy(csv_read))
    elif command == '2':
        csv_read = read_csv(file_path=r'C:\Users\Abdurakhim\Desktop\Corp_Summary.csv', delimiter=';')
        print(show_dep_report(csv_read))
    elif command == '3':
        file_path_to_save = input('Выбирите название файла и путь, где нужно схранить файл: ')
        save_results_into_csv(file_path_to_save)

# Проверка 3-го задания
# save_results_into_csv('C:\\Users\\Abdurakhim\\Desktop\\res2.csv')
