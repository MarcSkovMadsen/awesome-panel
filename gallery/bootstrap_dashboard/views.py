import pathlib
from typing import List, NamedTuple

import numpy as np
import pandas as pd
import param
from plotly import express as px

import awesome_panel.express as pnx
import panel as pn

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"


class Dashboard:
    def __init__(self, name="Dashboard"):
        chart_data = {
            "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
            "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
        }
        self.chart_data = pd.DataFrame(chart_data)

        table_data = [
            (1001, "Lorem", "ipsum", "dolor", "sit"),
            (1002, "amet", "consectetur", "adipiscing", "elit"),
            (1003, "Integer", "nec", "odio", "Praesent"),
            (1003, "libero", "Sed", "cursus", "ante"),
            (1004, "dapibus", "diam", "Sed", "nisi"),
            (1005, "Nulla", "quis", "sem", "at"),
            (1006, "nibh", "elementum", "imperdiet", "Duis"),
            (1007, "sagittis", "ipsum", "Praesent", "mauris"),
            (1008, "Fusce", "nec", "tellus", "sed"),
            (1009, "augue", "semper", "porta", "Mauris"),
            (1010, "massa", "Vestibulum", "lacinia", "arcu"),
            (1011, "eget", "nulla", "Class", "aptent"),
            (1012, "taciti", "sociosqu", "ad", "litora"),
            (1013, "torquent", "per", "conubia", "nostra"),
            (1014, "per", "inceptos", "himenaeos", "Curabitur"),
            (1015, "sodales", "ligula", "in", "libero"),
        ]
        self.table_data = pd.DataFrame(
            table_data, columns=["#", "Header", "Header", "Header", "Header"]
        ).set_index("#")

    def _chart(self):
        fig = px.line(self.chart_data, x="Day", y="Orders")
        fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
        fig.layout.autosize = True
        fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
        fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
        return pn.pane.Plotly(fig)

    def _table(self):
        return pn.Row(self.table_data, sizing_mode="stretch_width")

    def view(self, name="Dashboard"):
        return pn.Column(
            pn.pane.Markdown("## Dashboard"),
            self._chart(),
            pn.pane.Markdown("## Section Title"),
            self._table(),
            sizing_mode="stretch_width",
            name=name,
        )


def markdown_from_file(path: pathlib.Path, name) -> pn.Pane:
    with open(path, "r") as file:
        text = file.read()

    return pn.pane.Markdown(text, name=name)


def customers_view(name="Customers"):
    path = pathlib.Path(__file__).parent / "templates" / "customers.html"
    with open(path, "r") as file:
        template_html = file.read()
    app = pn.Template(template_html)
    app.add_variable("title", name)
    return pn.Column(app, name=name)


# class PageConfig(NamedTuple):
#     name: str
#     font_awesome_class: str
#     pane: pn.Pane


# PAGE_CONFIGS = [
#     PageConfig("Dashboard", "fas fa-home", Orders().view()),
#     PageConfig("Products", "far fa-file", Products()),
#     PageConfig("Customers", "fas fa-file", simple()),
#     PageConfig("Reports", "fas fa-file", pn.pane.Markdown("Reports")),
#     PageConfig("Integrations", "fas fa-file", pn.pane.Markdown("Integrations")),
#     PageConfig("About", "fas fa-file", markdown_from_file(ABOUT_PATH)),
# ]

