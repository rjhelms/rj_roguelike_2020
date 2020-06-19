import tcod


def main():
    screen_width = 80
    screen_height = 50

    tcod.console_set_custom_font(
        "arial10x10.png",
        tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD,
    )

    with tcod.console_init_root(
        w=screen_width,
        h=screen_height,
        title="Yet Another Roguelike Tutorial",
        order="F",
        vsync=True
    ) as root_console:
        while True:
            root_console.print(x=1,y=1,string="@")

            tcod.console_flush()

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()
