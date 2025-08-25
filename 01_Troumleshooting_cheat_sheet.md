**Markdown-шпаргалка для подготовки к Linux/DevOps секции Troubleshooting AVITO**:

````markdown
# 📌 Linux/DevOps Interview Cheat Sheet

## 1. Общие моменты
- Всегда проговаривай вслух, что делаешь.
- Пользуйся `man` вместо Google.
- Если непонятно → рассуждай логически.

---

## 2. Базовый обзор системы

### CPU / RAM / Disk
```bash
lscpu
free -h
df -h
lsblk
````

### Почему в `free` мало свободной памяти?

* Linux кеширует (page cache).
* Колонка `available` = реально доступная память.

---

## 3. Виртуализация и контейнеры

### Определить: ВМ или контейнер

```bash
ps -ef | egrep "docker|containerd|pause"
systemd-detect-virt   # если есть
cat /proc/1/cgroup
```

* PID 1 → `systemd` = скорее ВМ.
* PID 1 → `bash` или `python` = контейнер.

---

## 4. Работа с процессами

### Убить все процессы с PID, оканчивающимися на `00`

```bash
ps -eo pid,cmd | grep '00$' | awk '{print $1}' | xargs kill
```

### Найти процессы, работающие > 3 дней

```bash
ps -eo pid,etime,cmd | grep '^[ ]*[0-9]'
```

* В колонке `etime` ищи `days`.

---

## 5. Пользователи и сессии

### Кто в системе

```bash
who
w
```

### Если `who` не показывает пользователя

* Проверить `/var/run/utmp`.
* Отдебажить:

```bash
strace who
```

* Перелогиниться или пересоздать `utmp`.

---

## 6. Работа с логами

### Восстановить удалённый `access.log` (без рестарта nginx)

```bash
lsof -p <NGINX_PID> | grep access.log
cp /proc/<PID>/fd/<FD> ./recovered_access.log
```

### Найти самый долгий запрос с кодом 200

```bash
awk '$9 == 200 {print $10}' access.log | sort -nr | head -n1
```

(где `$9` = код ответа, `$10` = время запроса)

---

## 7. Итог собеседования

* Тестируют troubleshooting, а не только теорию.
* Этапы:

  1. Linux/системный уровень.
  2. Coding (Python/Go).
  3. System Design (High/Low level).
