import PySimpleGUI as sg
from initial_ideas import feel_bored, web_search, youtube_search
import webbrowser


def window_two(task):
    sg.theme('Material1')

    web_results_titles, web_results_links = web_search(task)
    youtube_results_titles, youtube_results_links = youtube_search(task)

    layout = [
        [sg.Push(), sg.Text(task, font=('Roboto', 15, 'bold'), text_color='#FF7722', auto_size_text=True), sg.Push()],
        [sg.Push(), sg.Text("YouTube results", font=('Roboto', 15, 'bold'), text_color='#C87A8A'), sg.Push()],
        [sg.HorizontalSeparator()],
        [sg.Column(
            [[sg.Text(youtube_results_titles[x], font=('Roboto', 15), auto_size_text=True, enable_events=True, size=(60, 2),
                      tooltip=youtube_results_links[x], key=f'URL {youtube_results_links[x]}', text_color='#6F848E' if x%2 else '#737474')] for x in
             range(len(youtube_results_titles))], scrollable=True)],

        [sg.Push(), sg.Text("Web search results", font=('Roboto', 15, 'bold'), text_color='#C87A8A'), sg.Push()],
        [sg.HorizontalSeparator()],
        [sg.Column(
            [[sg.Text(web_results_titles[x], font=('Roboto', 15), auto_size_text=True, enable_events=True, size=(60, 2),
                      tooltip=web_results_links[x], key=f'URL {web_results_links[x]}', text_color='#6F848E' if x%2 else '#737474')] for x in
             range(len(web_results_titles))], scrollable=True)]
    ]

    window = sg.Window('Solutions for you!', layout, margins=(20, 20), resizable=True, element_padding=(10, 10), location=(20, 20))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event.startswith('URL '):
            url = event.split(' ')[1]
            webbrowser.open_new_tab(url)
    window.close()


def window_one():
    sg.theme('Material1')

    layout = [[sg.Push(), sg.Text("Feel bored?", font=('Roboto', 50, 'bold'), text_color='#6F295B'), sg.Push()],
              [sg.Push(), sg.Button(button_text='CLICK ME', key='-clickme-', font=('Roboto', 20), border_width=0),
               sg.Push()],
              [sg.Push(), sg.pin(
                  sg.Text('Wonderful! I found an interesting task for you', font=('Roboto', 20), visible=False,
                          key='-prompt-')), sg.Push()],
              [sg.Push(),
               sg.pin(sg.Text(key='-task-', visible=False, font=('Roboto', 30, 'bold'), auto_size_text=True, text_color='#FF7722')),
               sg.Push()],
              [sg.Push(), sg.pin(sg.Text('Unsure how? Click here to see suggestions.', font=('Roboto', 15), visible=False,
                                         key='-more-info-', text_color='#B31942', enable_events=True)), sg.Push()],
              ]

    window = sg.Window('::Are you bored::?', layout=layout, margins=(30, 30), resizable=True, element_padding=(20, 20), location=(20, 20))

    while True:
        clicked = False
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-clickme-':
            task = feel_bored()
            window['-prompt-'].update(visible=True)
            window['-task-'].update(visible=True, value=task)
            window['-more-info-'].update(visible=True)
        elif event == '-more-info-':
            clicked = True
            break
    window.close()
    if clicked:
        window_two(task)


if __name__ == '__main__':
    window_one()
