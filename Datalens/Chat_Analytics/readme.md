**Дашборд в Datalens для анализа активности телеграм-чата.**

Проект был реализован на основе статей [раз](https://cloud.yandex.ru/blog/posts/2023/04/telegram-chat-analytics?utm_source=telegram&utm_medium=post_&utm_campaign=revealthedata) и [два](https://skillbox.ru/media/code/parsim-dannye-v-telegram-na-python-chast-1/).

На данном этапе реализовн дашборд, подключённый к статичному csv файлу. Файл собран с помощью [python-скрипта](https://github.com/alenakot/portfolio_BI/blob/main/Datalens/Chat_Analytics/Scrapper.py). 

Использовались такие python библиотеки как:
- pandas
- telethon

Ссылка на готовый дашборд [тут](https://datalens.yandex.ru/yiikuv5tgvx8o-chat-analytics).

Вопросы, на которые отвечает дашборд:

- активность участников чата по дням, дням недели и по часам;
- id наиболее активных участникв;
- наиболее популярные вакансии в чате;
- как часто люди отвечают на сообщения.

[Скрин](https://github.com/alenakot/portfolio_BI/blob/main/Datalens/Chat_Analytics/screen_1.png) того, как выглядит дашборд в тёмной теме Datalens.

[Скрин](https://github.com/alenakot/portfolio_BI/blob/main/Datalens/Chat_Analytics/screen_2.png) того, как выглядит дашборд с тултипами и раскрытым календарём.

Планы по развитию проекта:
- автоматизация сбора данных;
- сбор дополнительной информации из чата;
- автоматизация обновления дашборда. 
