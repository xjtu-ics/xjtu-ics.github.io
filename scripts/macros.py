import pandas as pd
import re
def define_env(env):
    @env.macro
    def read_schedule_csv(csv_path):
        df = pd.read_csv(csv_path, dtype=str)
        df['theme'] = df['theme'].fillna('TBA')
        df.fillna('', inplace=True)
        # only select Lecture
        df = df[(df['title'] == 'Lecture') | (df['title'] == 'Lab')]
        df = df.drop(columns=['title', 'location'])
        df.rename(columns={'theme': 'Lecture', 'extra': "Labs", "pptLink" : "Materials"}, inplace=True)
        df['Materials'] = df['Materials'].apply(lambda str: f"[:material-presentation-play: Slides]({str}){{.md-button}}" if str != "" else "")
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        markdown_table = df.to_markdown(index=False, tablefmt="github")
        lines = markdown_table.split("\n")
        header = lines[0]
        separator = lines[1] 

        centered_separator = re.sub(r"(---+)", lambda x: f":{x.group(1)}:", separator)
        lines[1] = centered_separator

        centered_markdown_table = "\n".join(lines)        
        return centered_markdown_table

    @env.macro
    def read_office_hour_csv(csv_path):
        df = pd.read_csv(csv_path, dtype=str)
        df.fillna('', inplace=True)
        markdown_table = df.to_markdown(index=False, tablefmt="github")
        lines = markdown_table.split("\n")
        header = lines[0]
        separator = lines[1] 

        centered_separator = re.sub(r"(---+)", lambda x: f":{x.group(1)}:", separator)
        lines[1] = centered_separator

        centered_markdown_table = "\n".join(lines)        
        return centered_markdown_table