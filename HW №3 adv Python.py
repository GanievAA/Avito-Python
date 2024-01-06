# Task #1
import asyncio
from asyncio import Task
from typing import Callable, Coroutine, Any

async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        return await f()
    
    elif isinstance(f, Task):
        return await f
        
    elif isinstance(f, Coroutine):
        task = asyncio.create_task(f)
        return await task
        
    else:
        raise ValueError('invalid argument')

# Task #2
async def magic_func() -> int:
    return 42

async def fix_this_code() -> int:
    return await magic_func()

# Task #3
import asyncio
from dataclasses import dataclass
from typing import Awaitable


@dataclass
class Ticket:
    number: int
    key: str


async def coroutines_execution_order(coros: list[Awaitable[Ticket]]) -> str:
    # Необходимо выполнить все полученные корутины, затем упорядочить их результаты
    # по полю number и вернуть строку, состоящую из склеенных полей key.
    #
    # Пример:
    # r1 = Ticket(number=2, key='мыла')
    # r2 = Ticket(number=1, key='мама')
    # r3 = Ticket(number=3, key='раму')
    #
    # Результат: 'мамамылараму'
    #
    results = []
    for cor in coros:
        result = await cor
        results.append(result)
    results = sorted(results, key=lambda x: x.number)
    results = [x.key for x in results]
    return ''.join(results)

# Task #4
async def task_1(i: int):
    print(1)
    if i == 0:
        return

    if i > 5:
        await task_2(i // 2)
    else:
        await task_2(i - 1)


async def task_2(i: int):
    print(2)
    if i == 0:
        return

    if i % 2 == 0:
        await task_1(i // 2)
    else:
        await task_2(i - 1)


async def coroutines_execution_order(i: int = 42) -> int:
    # Отследите порядок исполнения корутин при i = 42 и верните число, соответствующее ему.
    #
    # Когда поток управления входит в task_1 добавьте к результату цифру 1, а когда он входит в task_2,
    # добавьте цифру 2.
    #
    # Пример:
    # i = 7
    # return 12212
    await task_1(i)

    return 122122122

# Task #5
import asyncio
from typing import Coroutine

async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    # Функция принимает на вход корутину, которую необходимо запустить, однако иногда она выполняется
    # слишком долго, это время необходимо ограничить переданным на вход количеством секунд.
    
    async with asyncio.timeout(max_execution_time):
        await coro


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    # Функция эквивалентна limit_execution_time, но корутин на вход приходит несколько.
    
    tasks = [asyncio.create_task(coro) for coro in coros]
    
    done, pending = await asyncio.wait(tasks, timeout=max_execution_time)
    
    for t in pending:
        t.cancel()