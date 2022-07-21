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


st.subheader("1 - Concept de départ (0 - 30 points)")
st.text("""On dit souvent avec raison que les idées n’ont pas de valeur, seule compte l’exécution.
Ce n’est pas entièrement vrai. Certaines idées sont quand même plus fécondes que d’autres
et surtout certaines idées sont mieux à
même d’attirer les bons talents et les capitaux, ce qui est clé pour le démarrage d’une startup.""")
st.markdown("##")

g_concept = st.slider('Combien de point attribuons nous au concepts de base ?', 0, 30, 0)

g_concep_e = 0
g_concep_a = 0
g_concep_n = 0

if(g_concept > 0):
    st.markdown("##")
    st.markdown("##")
    g_concep_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_concept, 0)
    g_concep_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_concept, 0)
    g_concep_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_concept, 0)

#st.write("I'm ", age, 'years old')

st.subheader("2 - Validation du concept (entre 0 et 120 points) ")
st.text("""Parfois au moment de la formation de la société,
le concept de départ n’est qu’une ébauche sans rien de plus.
Parfois certains associés ont déjà travaillé plusieurs semaines ou mois pour réunir des éléments donnant de la consistance à l’idée de départ.
Il peut s’agir d’un business plan détaillé, d’une étude de marché auprès de clients potentiels, d’une maquette technique, voire d’un vrai prototype opérationnel.
Ces éléments peuvent fournir des métriques importantes pour crédibiliser le projet et le rendre de fait (même si c’est en grande partie illusoire) moins risqué.
Cela peut attirer d’autant plus talents et capitaux et donc a une valeur importante pour le projet.""")

st.markdown("##")
g_val_concept = st.slider('Combien de point attribuons nous à la validation du concept ?', 0, 120, 0)

g_val_concept_e = 0
g_val_concept_a = 0
g_val_concept_n = 0

if(g_val_concept > 0):
    st.markdown("##")
    st.markdown("##")
    g_val_concept_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_val_concept, 0)
    g_val_concept_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_val_concept, 0)
    g_val_concept_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_val_concept, 0)
#st.write("I'm ", age, 'years old')

st.subheader("3 - Rôles techniques (entre 70 et 130 points) et rôles généralistes (entre 90 et 110 points)")
st.text("""On attend d’un fondateur qui a un profil généraliste qu’en fonction des besoins de la startup,
il puisse faire potentiellement du commercial, de la finance, des opérations ou du marketing.
Il est en effet souvent difficile de figer à l’avance quelle sera la contribution exacte des fondateurs généralistes, cette capacité de traiter des problèmes très différents étant la marque de fabrique des bons entrepreneurs.
Pour la technique par contre, on ne peut pas s’improviser dessus et seuls les fondateurs qui ont les compétences adéquates pourront prétendre contribuer utilement dans ce domaine.
D’où l’idée de séparer d’un côté les fondateurs qui auront principalement une contribution technique et de l’autre les généralistes qui s’occuperont du reste.
Les besoins généralistes sont sensiblement les mêmes dans toutes les startups, donc la variabilité spécifique liée au projet est assez limité (entre 90 et 110 points).
Par contre, selon la nature du projet, l’impact de la technique sur le succès du projet peut varier énormément d’où une variabilité nettement plus importante (entre 70 et 130 points).
""")

st.markdown("##")
g_role_tech = st.slider('Combien de point attribuons nous aux roles Tech ?', 70, 130, 70)

g_role_tech_e = 0
g_role_tech_a = 0
g_role_tech_n = 0

if(g_role_tech > 70):
    g_role_tech_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_role_tech, 0)
    g_role_tech_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_role_tech, 0)
    g_role_tech_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_role_tech, 0)

g_role_tech = st.slider('Combien de point attribuons nous aux roles Généraliste ?', 90, 110, 90)

#st.write("I'm ", age, 'years old')

st.subheader("4 - Position de CEO (entre 40 et 100 points)")
st.text("""Une équipe qui n’a pas clarifié dès le départ qui est censé trancher en dernier ressort fait fuir les investisseurs.
Le choix de celui qui sera le CEO de la startup est un élément très structurant du projet. Le CEO est l’interlocuteur naturel des investisseurs financiers.
Ils seront très sensibles à son profil et cela pèsera très lourd dans leur décision d’investir. Outre insuffler la vision et la culture d’entreprise,
les VCs attendent aussi du CEO qu’il puisse prendre les décisions difficiles, notamment celles où il y a désaccord entre co-fondateurs.

A noter que dans l’étude Galion, parmi les équipes qui ont choisi une répartition inégalitaire, dans 80% des cas, le CEO avait plus de capital que les autres.

Pour toutes ces raisons, l’impact particulier du CEO dans la bonne marche du projet justifie un bonus en capital lié à ce rôle.
Le montant de ce bonus devra être modulé selon l’expérience antérieure du fondateur comme CEO, avec l’idée que cette expérience est censée être un prédicteur de la contribution à venir.
De 40 points si c’est la première fois qu’il est dans ce rôle, le bonus peut monter jusqu’à 100 points pour quelqu’un qui peut justifier d’une expérience de CEO longue et réussie dans des contextes très complexes.""")

g_ceo = st.slider('Combien de point attribuons nous au role de CEO ?', 40, 100, 40)


st.subheader("Expérience antérieure pertinente (entre 0 et 100 points)")
st.text("""Réussir à faire grandir une startup nécessite des compétences très particulières.
Autrement dit, avoir des expériences réussies dans d’autres contextes professionnels n’est pas un bon prédicteur de la réussite dans une startup.

Par contre, les statistiques montrent que les serial-fondateurs de startup deviennent de plus en plus efficaces au fil de leurs projets (d’où l’intérêt de commencer jeune sa carrière d’entrepreneur !).
Les VCs sont très sensibles à ce point dans leur décision d’investir.
En conséquence, seule l’expérience comme fondateur d’une startup a été retenue ici. Le montant du bonus dépend bien évidemment de la trajectoire des startups précédentes.
On peut compter 20 points quelqu’un qui a réussi à lever quelques millions d’euros, jusqu’à 100 points ou plus pour celui qui a conduit une belle licorne jusqu’à une sortie réussie.""")

g_ceo = st.slider('Combien de point attribuons nous à nos experiences antérieurs ?', 0, 100, 0)
#st.write("I'm ", age, 'years old')
st.subheader("5 - Expertise sectorielle (entre 0 et 20 points)")
st.text("""UPour certains projets, une expertise sectorielle permet d’éviter certains tâtonnements et de gagner du temps sur les premières itérations du projet.
Néanmoins, sur le long terme, ce type d’expertise sectorielle est souvent surestimée, car les fondateurs peuvent assez facilement recruter ces experts comme employés ou consultants.
D’où un bonus assez limité pour cet apport.""")

g_ceo = st.slider('Combien de point attribuons nous à notre exp sectorielle ?', 0, 20, 0)


#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
#st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)









#df = pd.DataFrame(data)
