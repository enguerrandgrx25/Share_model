# import module
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import notion_df

from PIL import Image


st.set_page_config(
    page_title="Hello hello",
    page_icon="👋",
)

image = Image.open('cyna.jpg')

st.image(image)

# Title
st.title("Méthode Galion")


st.subheader("Concept de départ (0 - 30 points)")
st.text("""On dit souvent avec raison que les idées n’ont pas de valeur, seule compte l’exécution. Ce n’est pas entièrement vrai. Certaines idées sont quand même plus fécondes que d’autres et surtout certaines idées sont mieux à
même d’attirer les bons talents et les capitaux, ce qui est clé pour le démarrage d’une startup.""")

g_concept = st.slider('Combien de point attribuons nous au concepts de base ?', 0, 30, 5)
#st.write("I'm ", age, 'years old')

st.subheader("Validation du concept (entre 0 et 120 points) ")
st.text("""Parfois au moment de la formation de la société, le concept de départ n’est qu’une ébauche sans rien de plus. Parfois certains associés ont déjà travaillé plusieurs semaines ou mois pour réunir des éléments donnant de la consistance à l’idée de départ. Il peut s’agir d’un business plan détaillé, d’une étude de marché auprès de clients potentiels, d’une maquette technique, voire d’un vrai prototype opérationnel. Ces éléments peuvent fournir des métriques importantes pour crédibiliser le projet et le rendre de fait (même si c’est en grande partie illusoire) moins risqué. Cela peut attirer d’autant plus talents et capitaux et donc a une valeur importante pour le projet.""")

g_val_concept = st.slider('Combien de point attribuons nous à la validation du concept ?', 0, 120, 10)
#st.write("I'm ", age, 'years old')

st.subheader("Rôles techniques (entre 70 et 130 points) et rôles généralistes (entre 90 et 110 points)")
st.text("""On attend d’un fondateur qui a un profil généraliste qu’en fonction des besoins de la startup, il puisse faire potentiellement du commercial, de la finance, des opérations ou du marketing. Il est en effet souvent difficile de figer à l’avance quelle sera la contribution exacte des fondateurs généralistes, cette capacité de traiter des problèmes très différents étant la marque de fabrique des bons entrepreneurs. Pour la technique par contre, on ne peut pas s’improviser dessus et seuls les fondateurs qui ont les compétences adéquates pourront prétendre contribuer utilement dans ce domaine. D’où l’idée de séparer d’un côté les fondateurs qui auront principalement une contribution technique et de l’autre les généralistes qui s’occuperont du reste. Les besoins généralistes sont sensiblement les mêmes dans toutes les startups, donc la variabilité spécifique liée au projet est assez limité (entre 90 et 110 points). Par contre, selon la nature du projet, l’impact de la technique sur le succès du projet peut varier énormément d’où une variabilité nettement plus importante (entre 70 et 130 points).
""")

g_role_tech = st.slider('Combien de point attribuons nous aux roles Tech ?', 0, 30, 5)
g_role_tech = st.slider('Combien de point attribuons nous aux roles Generaliste ?', 0, 30, 5)

#st.write("I'm ", age, 'years old')

st.subheader("Concept de départ (0 - 30 points)")
st.text("""On dit souvent avec raison que les idées n’ont pas de valeur, seule compte l’exécution. Ce n’est pas entièrement vrai. Certaines idées sont quand même plus fécondes que d’autres et surtout certaines idées sont mieux à
même d’attirer les bons talents et les capitaux, ce qui est clé pour le démarrage d’une startup.""")

g_concept = st.slider('Combien de point attribuons nous au concepts de base ?', 0, 30, 5)
#st.write("I'm ", age, 'years old')


#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)


st.header("Page 2 - Intrusion detection dashboard")






#df = pd.DataFrame(data)
