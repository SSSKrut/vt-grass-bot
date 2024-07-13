# VT Grass Bot

Telegram bot for posting photos of grass, flowers and trees from internet.

> [!NOTE]
> I am a dummy-dumb-dumb, so this project may have problems with optimization, finding photos online, posting, etc. Use it at your own risk!

## Dependencies

- Python 3.12
- Poetry (see [installation instructions](https://python-poetry.org/docs/#installation))

## Feature set

- [x] Make first realization
- [ ] Posting random plant image from internet
- [ ] Post it at a certain interval
- [ ] Posting weather for some location
- [ ] Dockerization
- [ ] Localization via .json
- [ ] Admin tools

## Configuration

Make a `.config.yaml` file with this useful but not obligatory options:
- ```admins: [<admin_id>, <another_admin_id>]```
- ```license: 'MIT license...'```
- ...

and `token: '1234:123123123'` with your bot's token from Telegram.

> [!TIP]
> If you have any difficulties creating a config file, take a look at the [finished one](./config.yaml) in the repository.

## Start bot

Use a .venv to avoid trashing your packages. To create it and use:

```$ poetry install```
```$ source .venv/bin/activate``` or ```$ poetry shell```

After that you can start your bot's init:

```$ python bot.py```
