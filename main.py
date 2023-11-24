from services.sender.send import sender, make_list_for_send

lst_for_send = make_list_for_send()


def main():
    sender(lst_for_send)


if __name__ == "__main__":
    main()
