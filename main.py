from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from playerExtraction import find_player  # Import your function from playerExtraction.py

class PlayerApp(App):
    def build(self):
        # Create the layout
        layout = BoxLayout(orientation='vertical')

        # Input field for the player name
        self.input = TextInput(hint_text="Enter Player Name", multiline=False)

        # Button to trigger the search
        button = Button(text="Search", on_press=self.search_player)

        # Label to display the result
        self.output = Label(text="")

        # Add widgets to the layout
        layout.add_widget(self.input)
        layout.add_widget(button)
        layout.add_widget(self.output)

        return layout

    def search_player(self, instance):
        # Get the player name from the input field
        player_name = self.input.text.strip()

        # Call the find_player function from playerExtraction.py
        result = find_player(player_name)

        # Display the result in the output label
        self.output.text = result

if __name__ == "__main__":
    PlayerApp().run()