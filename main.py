import discord
from discord.ext import commands
from lg import *
from lgGame import *
from etudiants import *

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
global gamesDic

@bot.event
async def on_ready():
    gamesDic = loadGames()
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)
    print("Ready !")


@bot.command()
async def lg(ctx):
    '''Affiche les stats d'un joueur'''
    id = ctx.message.author.id
    
    if not hasAGame(id):
        embed = discord.Embed(title="Erreur, une partie est déjà en cours !", colour=None, color=None, type='rich', url=None, description="/lg reset pour supprimer la partie en cours.", timestamp=None)
        embed.add_field(name="Field", value="Field text")
        await ctx.send(embed=embed)

@bot.tree.command(name="login")
async def login(interaction: discord.Interaction, nom: str, numeroEtudiant: int):
    await interaction.response.send_message(f"Tu t'es bien enregistré avec ces infos: **Nom:** {nom}, **Numéro étudiant:** {numeroEtudiant}", ephemeral=True)

@bot.command()
async def resetData(ctx):
    storeEtudiantsListe([])

@bot.command()
async def r(ctx, *nom):
    txt = ''
    for elem in nom:
        txt += " " + elem
    user = ctx.message.author
    etudiant = generateEtudiant(txt, user.id)
    etudiantsListe = loadEtudiantsListe()
    if etudiant not in etudiantsListe:
        etudiantsListe.append(etudiant)
        storeEtudiantsListe(etudiantsListe)
        await user.send(f"Bravo {txt}, tu t'es bien inscrit !")
        return
    await user.send(f"Il y a eu une erreur lors de ton inscription.")

@bot.command()
async def notes(ctx):
    etudiantsList = loadEtudiantsListe()
    etudiant = getEtudiant(ctx, etudiantsList)

    if not etudiant:
        await ctx.send("Ton profil n'est pas dans ma base de données, fais **/register [Nom Prénom]** pour en créer un !")
        return

    embed = generateProfile(etudiant)
    await ctx.send(embed=embed)

@bot.command()
async def ajouterNote(ctx):
    etudiantsList = loadEtudiantsListe()
    etudiant = getEtudiant(ctx, etudiantsList)

    if not etudiant:
        await ctx.send("Ton profil n'est pas dans ma base de données, fais **/register [Nom Prénom]** pour en créer un !")
        return

    def generateOptions(etudiant):
        list = []
        for matiere in etudiant.getMatieresListe():
            list.append(discord.SelectOption(label=matiere.getNom(),value=len(list)))
        return list

    class SelectMatiere(discord.ui.View):
        @discord.ui.select (
            placeholder="Sélectionne la matière",
            options=generateOptions(etudiant)
        )

        async def select_callback(self, interaction, select):
            await ctx.send("Entre le nom de la note, puis sa valeur (par exemple, CC 16)")
            channel = ctx.channel

            def check(message):
                return message.author == ctx.message.author and message.channel == channel

            msg = await bot.wait_for('message', check=check)
            
            l = msg.content.split(" ")

            if len(l) < 2:
                await ctx.send(f"Erreur, format attendu: [NomNote] [Note]")
                return

            try:
                nom, note = l[0], int(l[1])
            except ValueError:
                await ctx.send(f"Erreur, format attendu: [NomNote] [Note]")
                return

            matiereSelectionee = etudiant.getMatieresListe()[int(select.values[0])]

            if not note:
                await ctx.send(f"La note {nom} de la matière {matiereSelectionee.getNom()} n'existe pas.")
                return

            matiereSelectionee.setNote(nom, note)
            etudiant.updateMatiere(matiereSelectionee)
            
            etudiantsListe = updateEtudiantList(etudiantsList, etudiant)
            storeEtudiantsListe(etudiantsListe)
            await ctx.send("La note a bien été ajoutée.")

    view = SelectMatiere()
    await ctx.send(view=view)
    
@bot.command()
async def voirMoyennes(ctx):
    etudiantsList = loadEtudiantsListe()
    etudiant = getEtudiant(ctx, etudiantsList)

    if not etudiant:
        await ctx.send("Ton profil n'est pas dans ma base de données, fais **/register [Nom Prénom]** pour en créer un !")
        return
    
    embed = generateMoyennes(etudiant)
    await ctx.send(embed=embed)



bot.run("Nzg2MjYyOTM1Mzc4MTk4NTQ5.G0gXJM.TeqvyIJrRg2SB9hI5omMeL3zE6GOv4q_wbIKm0")
