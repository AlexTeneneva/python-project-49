### Hexlet tests and linter status:

[![Actions Status](https://github.com/AlexTeneneva/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AlexTeneneva/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/2e59aa1a90e835d1182b/maintainability)](https://codeclimate.com/github/AlexTeneneva/python-project-49/maintainability)

Brain games.
Это игра, включающая в себя 5 мини игр. У всех игр один сценарий:
1. Приветствие
2. Спрашивает имя
3. Описывает задание
4. Далее следует 3 вопроса
5. Если поступает не верный ответ, игра заканчивается. 
6. Если все ответы правильные - игрок выиграл

Для установки игры вам потребуется Python версии 3.6 и выше, Pip версии 19 и выше, poetry версии 1.2.0 и выше.

Инструкция по установке:
1. Необходимо установть окружение
2. Установить Poetry, далее командой в директории игры установка командой Poetry install
3. Собрать проект командой make build
4. Для установки приложения из пакетов нужна команда make packege-install


Теперь подробнее о каждой игре.
Название игры - это её запуск.
1. brain-even. Нужно ответить yes или no на вопрос четное ли число 
[![asciicast](https://asciinema.org/a/hMf2UfQUzIpKF6YdNs1z4R51N.svg)](https://asciinema.org/a/hMf2UfQUzIpKF6YdNs1z4R51N)

2. brain-calc. Нужно посчитать результат выражения
[![asciicast](https://asciinema.org/a/O9hXBnNLzBqPvhYeFh5Ciz14k.svg)](https://asciinema.org/a/O9hXBnNLzBqPvhYeFh5Ciz14k)

3. brain-gcd. Нужно указать наименьший общий делитель пары чисел
[![asciicast](https://asciinema.org/a/Y4sRuljJEhHSf1pVi3TdEBfDN.svg)](https://asciinema.org/a/Y4sRuljJEhHSf1pVi3TdEBfDN)

4. brain-progression. Дается прогрессия. Нужно указать недостающий ее элемент
[![asciicast](https://asciinema.org/a/hgxgZZ3KWkp2z7u84KE6FWf8e.svg)](https://asciinema.org/a/hgxgZZ3KWkp2z7u84KE6FWf8e)


5. brain-prime. Нужно ответить является ли данное число простым - yes или no
[![asciicast](https://asciinema.org/a/48J3C68SRfFOGPPTZvxXdTU1d.svg)](https://asciinema.org/a/48J3C68SRfFOGPPTZvxXdTU1d)