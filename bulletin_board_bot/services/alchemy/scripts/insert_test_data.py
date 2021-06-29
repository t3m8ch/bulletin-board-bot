import asyncio
import random
from time import sleep

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import create_async_engine

from bulletin_board_bot.config import cfg
from bulletin_board_bot.services.alchemy import AdTable

text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
       "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis " \
       "natoque penatibus et magnis dis parturient montes, nascetur " \
       "ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, " \
       "pretium quis, sem. Nulla consequat massa quis enim. Donec pede " \
       "justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim " \
       "justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum " \
       "felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. " \
       "Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. " \
       "Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. " \
       "Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. " \
       "Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. " \
       "Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper " \
       "ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, " \
       "tellus eget condimentum rhoncus, sem quam semper libero, sit amet " \
       "adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, " \
       "hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. " \
       "Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. " \
       "Etiam sit amet orci eget eros faucibus tincidunt. " \
       "Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. " \
       "Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, "


def generate_text(word_count: int) -> str:
    words = [
        random.choice(text.split())
        for _ in range(word_count)
    ]
    return " ".join(words)


async def insert_test_data_async(connection_str: str):
    engine = create_async_engine(connection_str, echo=True)
    async with engine.connect() as conn:
        for _ in range(100):
            await conn.execute(
                insert(AdTable).values(text=generate_text(30)[:300])
            )
            await conn.commit()
            sleep(0.1)  # it's so that there is a difference in time of creation


def insert_test_data():
    asyncio.run(insert_test_data_async(cfg.db_connection_str))


if __name__ == "__main__":
    insert_test_data()
