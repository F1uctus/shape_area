# Shape area calculation CLI utility

### Спецификация для shape_area.py

**Тип программы**: Консольное приложение

**Назначение программы**: Вычисление площади выпуклых многоугольников с произвольным количеством вершин.

Аргументы программы:

| Аргумент                                | Описание действия                     |
|-----------------------------------------|---------------------------------------|
| `-i`                                    | Запуск в интерактивном режиме         |
| Пары координат `x` `y` в кол-ве более 3 | Запуск в режиме одиночного исполнения |

**Алгоритм работы**:

Программа реализована на языке Python 3.
Вычисление площади происходит с помощью [формулы площади Гаусса](https://ru.wikipedia.org/wiki/Формула_площади_Гаусса). Алгоритм вычисления представлен в файле [`by_points.py`](https://github.com/F1uctus/shape_area/blob/main/by_points.py)

**Режимы работы**:

1) **Интерактивный режим**<br>
    1) Программа представляет собой циклическое консольное приглашение, работающее в качестве обработчика введёных команд.
    2) После ввода каждой команды отображается фигура и её площадь (изображение открывается стандартным средством просмотра изображений системы).
    3) Приглашение командной строки обозначается как `> `.
    4) Доступные команды интерактивного режима:

| Команда        | Описание действия                                             |
|----------------|---------------------------------------------------------------|
| `a` или `add`  |  Добавление точки на график, перерисовка фигуры и её площади. |
| `d` или `del`  |  Удаление точки с графика, перерисовка фигуры и её площади.   |
| `?` или `help` | Отображение консольной справки.                               |
| `x` или `exit` | Выход из программы.                                           |

<br>

2) **Режим одиночного исполнения**<br>
    1) Программа вычисляет площадь выпуклого многоугольника, построенного по указанным в аргументах точкам.
    2) Вывод фигуры программой происходит в виде её изображения на координатной плоскости.
    3) Вывод площади фигуры программой происходит в формате `Area is #`, где `#` - площадь.
