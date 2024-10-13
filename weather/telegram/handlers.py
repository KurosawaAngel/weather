from typing import Any

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)

from weather.api.client import OpenWeatherClient
from weather.api.enums import Units
from weather.telegram.keyboards import MAIN_KBD

router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Добро пожаловать в бота для отображения текущей погоды!\n"
        "Для просмотра используйте кнопку ниже или инлайн режим.",
        reply_markup=MAIN_KBD,
    )


@router.inline_query()
async def get_weather(query: InlineQuery, weather: OpenWeatherClient) -> Any:
    if not query.query:
        return
    coord = await weather.get_coordinates(query.query)
    if not coord:
        result = InlineQueryResultArticle(
            id="none",
            title=f"По вашему запросу {query.query} ничего не найдено",
            input_message_content=InputTextMessageContent(
                message_text=f"По вашему запросу {query.query} ничего не найдено"
            ),
        )
        return await query.answer([result], cache_time=7200)

    coord_city = coord[0]
    data = await weather.get_current_weather(
        lat=coord_city.lat, lon=coord_city.lon, lang="ru", units=Units.METRIC
    )

    result = InlineQueryResultArticle(
        id=coord_city.name,
        title=f"Погода в {coord_city.name}\n",
        input_message_content=InputTextMessageContent(
            message_text=f"<b>Погода в {coord_city.name}</b>\n"
            f"<b>Температура:</b> {data.temp} °C, {data.description}\n"
            f"<b>Ощущается как:</b> {data.feels_like} °C\n"
            f"<b>Влажность:</b> {data.humidity} %\n"
            f"<b>Давление:</b> {round(data.pressure/1.33)} мм. рт. ст."
        ),
    )

    return await query.answer([result], cache_time=600)
