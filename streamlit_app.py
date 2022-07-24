# import module
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import notion_df

from PIL import Image


st.set_page_config(
    page_title="Méthode Galion for CYNA",
    page_icon="👋",
)

image = Image.open('cyna.jpg')

st.image(image)

# Title
st.title("Méthode Galion")

st.error("""Le but de cet exercice est d'aborder des sujets important pour le succès de l'entreprise. Ces sujets ne sont pas forcement facile a aborder mais ils sont primordials""")

ok = st.checkbox("Are you ready / Ok ?")
if ok:

    st.subheader("1 - Concept de départ (0 - 30 points)")

    st.info("""On dit souvent avec raison que les idées n’ont pas de valeur, seule compte l’exécution.
    Ce n’est pas entièrement vrai. Certaines idées sont quand même plus fécondes que d’autres
    et surtout certaines idées sont mieux à
    même d’attirer les bons talents et les capitaux, ce qui est clé pour le démarrage d’une startup.
    Ici on donne des points pour le secteur choisi et le concept""")
    st.warning("Ici on donne des points pour le secteur choisi et le concept")


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

    st.info("""Parfois au moment de la formation de la société,
    le concept de départ n’est qu’une ébauche sans rien de plus.
    Parfois certains associés ont déjà travaillé plusieurs semaines ou mois pour réunir
    des éléments donnant de la consistance à l’idée de départ.
    Il peut s’agir d’un business plan détaillé,
    d’une étude de marché auprès de clients potentiels, d’une maquette technique,
    voire d’un vrai prototype opérationnel.
    Ces éléments peuvent fournir des métriques importantes pour crédibiliser
    le projet et le rendre de fait (même si c’est en grande partie illusoire) moins risqué.
    Cela peut attirer d’autant plus talents et capitaux et donc a une valeur importante pour le projet.""")

    st.warning("Ici on donne des points pour les elements qui crédibilisent le projet: business plan détaillé,d’une étude de marché auprès de clients potentiels, d’une maquette technique,voire d’un vrai prototype opérationnel.")

    st.markdown("##")
    g_val_concept = st.slider('Combien de point attribuons nous à la validation du concept ?', 0, 120, 0)

    g_val_concept_e = 0
    g_val_concept_a = 0
    g_val_concept_n = 0

    if(g_val_concept > 0):
        st.markdown("##")
        st.markdown("##")
        g_val_concept_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_val_concept, 0)
        g_val_concept_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_val_concept, 0)
        g_val_concept_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_val_concept, 0)
    #st.write("I'm ", age, 'years old')

    st.subheader("3.1 - Rôles généralistes (entre 90 et 110 points)")
    st.info("""On attend d’un fondateur qui a un profil généraliste qu’en fonction des besoins de la startup,
    il puisse faire potentiellement du commercial, de la finance, des opérations ou du marketing.

    Il est en effet souvent difficile de figer à l’avance quelle sera la contribution exacte des fondateurs généralistes,
    cette capacité de traiter des problèmes très différents étant la marque de fabrique des bons entrepreneurs.

    Les besoins généralistes sont sensiblement les mêmes dans toutes les startups,
    donc la variabilité spécifique liée au projet est assez limité (entre 90 et 110 points).
    """)
    st.warning("Ici on donne des points pour l'importance de la partie Business / Générale")

    st.markdown("##")

    g_role_gen = st.slider('Combien de point attribuons nous aux roles Généraliste ?', 90, 110, 90)

    g_role_gen_e = 0
    g_role_gen_a = 0
    g_role_gen_n = 0

    if(g_role_gen >= 90):
        g_role_gen_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_role_gen, 0)
        g_role_gen_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_role_gen, 0)
        g_role_gen_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_role_gen, 0)


    st.subheader("3.2 - Rôles techniques (entre 70 et 130 points)")
    st.info("""Pour la technique par contre, on ne peut pas s’improviser dessus et seuls les fondateurs
    qui ont les compétences adéquates pourront prétendre contribuer utilement dans ce domaine.
    D’où l’idée de séparer d’un côté les fondateurs qui auront principalement une contribution technique
    et de l’autre les généralistes qui s’occuperont du reste.
    Par contre, selon la nature du projet, l’impact de la technique sur le succès du projet peut varier
    énormément d’où une variabilité nettement plus importante (entre 70 et 130 points).
    """)

    st.warning("Ici on donne des points pour l'importance de la partie Technique")

    g_role_tech = st.slider('Combien de point attribuons nous aux roles Tech ?', 70, 130, 70)

    g_role_tech_e = 0
    g_role_tech_a = 0
    g_role_tech_n = 0

    if(g_role_tech >= 70):
        g_role_tech_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_role_tech, 0)
        g_role_tech_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_role_tech, 0)
        g_role_tech_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_role_tech, 0)



    #st.write("I'm ", age, 'years old')

    st.subheader("4 - Position de CEO (entre 40 et 100 points)")
    st.info("""Une équipe qui n’a pas clarifié dès le départ qui est censé trancher en dernier ressort fait fuir les investisseurs.
    Le choix de celui qui sera le CEO de la startup est un élément très structurant du projet. Le CEO est l’interlocuteur naturel des investisseurs financiers.
    Ils seront très sensibles à son profil et cela pèsera très lourd dans leur décision d’investir.
    Outre insuffler la vision et la culture d’entreprise, les VCs attendent aussi du CEO qu’il puisse prendre les décisions difficiles,
    notamment celles où il y a désaccord entre co-fondateurs.

    A noter que dans l’étude Galion, parmi les équipes qui ont choisi une répartition inégalitaire,
    dans 80% des cas, le CEO avait plus de capital que les autres.

    Pour toutes ces raisons, l’impact particulier du CEO dans la bonne marche du projet justifie un bonus en capital lié à ce rôle.
    Le montant de ce bonus devra être modulé selon l’expérience antérieure du fondateur comme CEO, avec l’idée que cette expérience est censée être un prédicteur de la contribution à venir.
    De 40 points si c’est la première fois qu’il est dans ce rôle, le bonus peut monter jusqu’à 100 points pour quelqu’un qui peut justifier d’une expérience de CEO longue et réussie dans des contextes très complexes.""")

    st.warning("Ici on donne des points pour l'experience en tant que CEO de celui qui sera CEO")


    g_ceo = st.slider('Combien de point attribuons nous au role de CEO ?', 40, 100, 40)

    g_ceo_e = 0
    g_ceo_a = 0
    g_ceo_n = 0

    if(g_ceo >= 40):
        g_ceo_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_ceo, 0)
        g_ceo_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_ceo, 0)
        g_ceo_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_ceo, 0)



    st.subheader("5 - Expérience antérieure pertinente (entre 0 et 100 points)")
    st.info("""Réussir à faire grandir une startup nécessite des compétences très particulières.
    Autrement dit, avoir des expériences réussies dans d’autres contextes professionnels n’est pas un bon prédicteur de la réussite dans une startup.

    Par contre, les statistiques montrent que les serial-fondateurs de startup deviennent de plus en plus efficaces au fil de leurs projets (d’où l’intérêt de commencer jeune sa carrière d’entrepreneur !).
    Les VCs sont très sensibles à ce point dans leur décision d’investir.
    En conséquence, seule l’expérience comme fondateur d’une startup a été retenue ici. Le montant du bonus dépend bien évidemment de la trajectoire des startups précédentes.
    On peut compter 20 points quelqu’un qui a réussi à lever quelques millions d’euros, jusqu’à 100 points ou plus pour celui qui a conduit une belle licorne jusqu’à une sortie réussie.""")

    st.warning("Ici on donne des points pour l'experience en Startup")


    g_exp_fnd = st.slider('Combien de point attribuons nous à nos experiences antérieurs ?', 0, 100, 0)

    g_exp_fnd_e = 0
    g_exp_fnd_a = 0
    g_exp_fnd_n = 0

    if(g_exp_fnd > 0):
        g_exp_fnd_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_exp_fnd, 0)
        g_exp_fnd_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_exp_fnd, 0)
        g_exp_fnd_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_exp_fnd, 0)




    st.subheader("6 - Expertise sectorielle (entre 0 et 20 points)")
    st.info("""Pour certains projets, une expertise sectorielle permet d’éviter certains tâtonnements et de gagner du temps sur les premières itérations du projet.
    Néanmoins, sur le long terme, ce type d’expertise sectorielle est souvent surestimée,
    car les fondateurs peuvent assez facilement recruter ces experts comme employés ou consultants.
    D’où un bonus assez limité pour cet apport.""")

    st.warning("Ici on donne des points pour l'experience dans la Cybersecurité")

    g_exp_sec = st.slider('Combien de point attribuons nous à notre exp sectorielle ?', 0, 20, 0)

    g_exp_sec_e = 0
    g_exp_sec_a = 0
    g_exp_sec_n = 0

    if(g_exp_sec > 0):
        g_exp_sec_a = st.slider('Combien de point attribuons nous à Alex ?', 0, g_exp_sec, 0)
        g_exp_sec_e = st.slider('Combien de point attribuons nous à Enguerrand ?', 0, g_exp_sec, 0)
        g_exp_sec_n = st.slider('Combien de point attribuons nous à Nathan ?', 0, g_exp_sec, 0)


    result = st.checkbox("Pret pour les resultats ?")
    if result:
        st.text("##")
        st.balloons()

        d = {
        "Type d'apport": ["Concept", "Validation du concept", "Roles Tech", "Roles Généraliste", "Position CEO",
        "Exp fondateurs", "Exp secteur"],
        'Min': [0, 0, 70, 90, 40, 0, 0],
        'Max': [30, 120, 130, 110, 100, 100, 20],
        'Score Alex': [g_concep_a, g_val_concept_a, g_role_tech_a, g_role_gen_a, g_ceo_a, g_exp_fnd_a, g_exp_sec_a],
        'Score Nathan': [g_concep_n, g_val_concept_n, g_role_tech_n, g_role_gen_n, g_ceo_n, g_exp_fnd_n, g_exp_sec_n],
        'Score Enguerrand': [g_concep_e, g_val_concept_e, g_role_tech_e, g_role_gen_e, g_ceo_e, g_exp_fnd_e, g_exp_sec_e]}

        df = pd.DataFrame(data=d)

        # CSS to inject contained in a string
        hide_dataframe_row_index = """
                    <style>
                    .row_heading.level0 {display:none}
                    .blank {display:none}
                    </style>
                    """

        # Inject CSS with Markdown
        st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

        st.dataframe(df)

        score_a = g_concep_a + g_val_concept_a + g_role_tech_a + g_role_gen_a + g_ceo_a + g_exp_fnd_a + g_exp_sec_a
        score_n = g_concep_n + g_val_concept_n + g_role_tech_n + g_role_gen_n + g_ceo_n + g_exp_fnd_n + g_exp_sec_n
        score_e = g_concep_e + g_val_concept_e + g_role_tech_e + g_role_gen_e + g_ceo_e + g_exp_fnd_e + g_exp_sec_e


        st.subheader("Voici donc la somme des scores par personne: ")
        st.text("Le score d'Alexandre est de: {}".format(score_a))
        st.text("Le score de Nathan est de: {}".format(score_n))
        st.text("Le score d'Enguerrand est de: {}".format(score_e))

        tt_score = score_a + score_n + score_e


        st.subheader("Voici donc la répartition proposé par la methode du Gallion: ")
        st.text("Alexandre: {}".format(round(score_a/tt_score, 2)))
        st.text("Nathan: {}".format(round(score_n/tt_score, 2)))
        st.text("Enguerrand: {}".format(round(score_e/tt_score, 2)))
