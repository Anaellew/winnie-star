from flask import Flask, request, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

citations = [
    "Un câlin est toujours la bonne taille.",
    "Parfois, les moindres choses prennent le plus de place dans votre cœur.",
    "Si vous vivez pour être cent, j’espère que je vis pour être cent moins un jour, de sorte que je n’ai jamais à vivre un jour sans vous.",
    "Les gens disent que rien n’est impossible, mais je ne fais rien tous les jours.",
    "Une journée sans ami est comme un pot sans une seule goutte de miel laissée à l’intérieur.",
    "C’est plus amusant de parler avec quelqu’un qui n’utilise pas de mots longs et difficiles, mais plutôt des mots courts et faciles comme » qu’en est-il du déjeuner?",
    "Si la personne à qui vous parlez ne semble pas écouter, soyez patient. Il se peut simplement qu’il ait un petit morceau de peluches dans l’oreille.",
    "Certaines personnes accordent beaucoup trop d’importance. Je pense que c’est de l’amour.",
    "Si jamais il arrive un jour où nous ne pouvons pas être ensemble, gardez-moi dans votre cœur, je resterai là pour toujours.",
    "Vous ne pouvez pas rester dans votre coin de forêt à attendre que d’autres viennent à vous. Tu dois aller les voir parfois.",
    "Je pense que nous rêvons pour ne pas être séparés si longtemps., Si nous sommes dans les rêves de l’autre, nous pouvons être ensemble tout le temps.",
    "Toute journée passée avec vous est ma journée préférée. Donc, aujourd’hui est mon jour préféré.",
    "Quand vous êtes un ours avec très peu de cerveau, et que vous pensez à des choses, vous trouvez parfois qu’une chose qui semblait très étrange à l’intérieur de vous est tout à fait différente quand elle sort au grand jour et que d’autres personnes la regardent.",
    "Quand vous allez après le miel avec un ballon, la grande chose est de ne pas laisser les abeilles savent que vous venez.",
    "Ne sous-estimez pas la valeur de ne rien faire, de simplement aller de l’avant, d’écouter toutes les choses que vous ne pouvez pas entendre et de ne pas déranger.",
    "Regardez toujours où vous allez. Sinon, vous pouvez marcher sur un morceau de forêt qui a été laissé de côté par erreur.",
    "Avant de commencer une chasse, il est sage de demander à quelqu’un ce que vous cherchez avant de commencer à le chercher.",
    "Je ne suis pas perdu car je sais où je suis. Mais cependant, où je suis peut être perdu.",
    "Quand vous voyez quelqu’un enfiler ses grosses bottes, vous pouvez être sûr qu’une aventure va se produire.",
    "Ceux qui sont intelligents, qui ont un cerveau, ne comprennent jamais rien.",
    "Quelle chance ai-je d’avoir quelque chose qui rend si difficile de dire au revoir.",
    "L’amour fait quelques pas en arrière peut-être encore plus pour céder la place au bonheur de la personne que vous aimez.",
    "Ce n’est pas très bon d’avoir quelque chose d’excitant, si vous ne pouvez pas le partager avec quelqu’un.",
    "Qu’y a-t-il de mal à savoir ce que vous savez maintenant et à ne pas savoir ce que vous ne savez pas avant plus tard?",
    "Quoi de plus important qu’un petit quelque chose à manger?",
    "Hier, quand c’était demain, c’était une journée trop excitante pour moi.",
    "Si les gens sont contrariés parce que vous avez oublié quelque chose, consolez—les en leur faisant savoir que vous n’avez pas oublié-vous ne vous souveniez tout simplement pas.",
    "Si possible, essayez de trouver un moyen de descendre qui n’implique pas d’aller bosse, bosse, bosse, à l’arrière de votre tête.",
    "J’arrive toujours là où je vais en m’éloignant de l’endroit où j’ai été."
]

dernieres_visites = {}

main_doc = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Winnie Star</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Winnie Star</h1>
    <form method="get" action="/ask">
        <h2>Demande conseil à Winnie</h2>
        <input type="submit" value="AskWinnie">
    </form>
</body>
</html>
'''

def quote_page(quote):
    return f'''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Winnie te parle</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
    <h1>Winnie Star</h1>
        <form method="get" action="/ask">
            <h2>Demande conseil à Winnie</h2>
            <input type="submit" value="AskWinnie">
        </form>
        <p>{quote}</p>
    </body>
    </html>
    '''

second_doc = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Winnie Star</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>Winnie Star</h1>
    <p>Winnie ne travaille qu'une fois par jour, reviens demain.</p>
</body>
</html>
'''

@app.route('/')
def home():
    return main_doc

@app.route('/ask')
def ask():
    ip = request.remote_addr
    today = datetime.now().date()

    last_visit = dernieres_visites.get(ip)

    if last_visit == today:
        return second_doc
    else:
        dernieres_visites[ip] = today
        quote = random.choice(citations)
        return quote_page(quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
