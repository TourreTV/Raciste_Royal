import discord
import os
import json

client = discord.Client()


def check_admin(mt):
    with open('admins.txt') as f:
        data = f.read()
    admins = json.loads(data);
    if (mt in admins):
        return (1)
    else:
        return (0)

def add_person(nom):
    nom1 = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    if nom1 not in lis:
        lis[nom1] = [0, 0, [0]]
    else:
        return (-1)
    with open('save.txt', 'w') as convert_file:
     convert_file.write(json.dumps(lis))

def add_raciste(nom, auth):
    nom = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    if nom in lis:
        if auth not in lis[nom]:
            lis[nom][1] += 1
            lis[nom].append(auth)
            if lis[nom][1] == 3:
                lis[nom] = [lis[nom][0] + 1, 0, lis[nom][2]]
                with open('save.txt', 'w') as convert_file:
                    convert_file.write(json.dumps(lis))
                return (-3)
            with open('save.txt', 'w') as convert_file:
                convert_file.write(json.dumps(lis))
            return (lis[nom][1])
        else:
            with open('save.txt', 'w') as convert_file:
                convert_file.write(json.dumps(lis))
            return (-2)
    else:
        with open('save.txt', 'w') as convert_file:
            convert_file.write(json.dumps(lis))
        return (-1)

def enl_raciste(nom, auth):
    nom = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    if nom in lis:
        if auth not in lis[nom][2]:
            lis[nom][2][0] += 1
            lis[nom][2].append(auth)
            if lis[nom][2][0] == 3:
                lis[nom] = [lis[nom][0] - 1, 0, [0]]
                with open('save.txt', 'w') as convert_file:
                    convert_file.write(json.dumps(lis))
                return (-3)
            with open('save.txt', 'w') as convert_file:
                convert_file.write(json.dumps(lis))
            return (lis[nom][2][0])
        else:
            with open('save.txt', 'w') as convert_file:
                convert_file.write(json.dumps(lis))
            return (-2)
    else:
        with open('save.txt', 'w') as convert_file:
            convert_file.write(json.dumps(lis))
        return (-1)


def check(nom):
    nom = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    if nom in lis:
        return lis[nom]
    else:
        return ("-1")
    
def noms():
    list_n = []
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    for i in lis:
        list_n.append(i)
    return list_n

def reset():
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    for i in lis:
        lis[i] = [0, 0, [0]]
    with open('save.txt', 'w') as convert_file:
     convert_file.write(json.dumps(lis))

def res(nom):
    nom = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    lis[nom] = [0, 0, [0]]
    with open('save.txt', 'w') as convert_file:
     convert_file.write(json.dumps(lis))

def del_person(nom):
    nom1 = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    if nom1 not in lis:
        del lis[nom1]
    else:
        return (-1)
    with open('save.txt', 'w') as convert_file:
        convert_file.write(json.dumps(lis))
    return (1)

@client.event
async def on_ready():
    print('Wesh {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$raciste '):
        nom = message.content.split()[1]
        func = add_raciste(nom, message.author.mention)
        if func == -1:
            await message.channel.send(f"{nom[0].upper()}{nom[1:]} est pas encore raciste, rajoute le avec '$ajoute {nom}'!")
        elif func == -2:
            await message.channel.send(f"T'as déjà voté sal arabe 🐀")
        elif func == -3:
            await message.channel.send(f"➕1️⃣ point de racisme pour {nom[0].upper()}{nom[1:]} c'est confirmé (3/3)")
        else:
            await message.channel.send(f"T'as voté pour donner un point de racisme à {nom[0].upper()}{nom[1:]} ({func}/3) ✏")

    if message.content.startswith('$deraciste '):
        nom = message.content.split()[1]
        func = enl_raciste(nom, message.author.mention)
        if func == -1:
            await message.channel.send(f"{nom[0].upper()}{nom[1:]} est pas encore raciste, rajoute le avec '$ajoute {nom}'!")
        elif func == -2:
            await message.channel.send(f"T'as déjà voté sal arabe 🐀")
        elif func == -3:
            await message.channel.send(f"➖1️⃣ point de racisme pour {nom[0].upper()}{nom[1:]} c'est confirmé (3/3)")
        else:
            await message.channel.send(f"T'as voté pour enlever un point de racisme à {nom[0].upper()}{nom[1:]} ({func}/3) ✏")
    
    if message.content.startswith('$ajoute '):
        nom = message.content.split()[1]
        if add_person(nom) == -1:
            await message.channel.send(f"{nom[0].upper()}{nom[1:]} existe deja ce raciste...")
        else:
            await message.channel.send(f"J'ai ajouté {nom} ce raciste!")
    
    if message.content.startswith('$score '):
        nom = message.content.split()[1]
        embedVar = discord.Embed(title="SCORE", description="Raciste ?? "+nom, color=0x00ff00)
        embedVar.add_field(name="Score", value=check(nom)[0], inline=False)
        if check(nom) == "-1":
            await message.channel.send(f"{nom[0].upper()}{nom[1:]} existe pas ce raciste...")
        else:
            await message.channel.send(embed=embedVar)
    
    if message.content.startswith('$commandes') or message.content.startswith('$help'):
        embedVar = discord.Embed(title="Commandes", description="📜", color=0x00ff00)
        embedVar.add_field(name="$commandes ou $help", value="Afficher les commandes", inline=False)
        embedVar.add_field(name="$raciste [nom]", value="Voter pour ajouter un point de racisme", inline=False)
        embedVar.add_field(name="$deraciste [nom]", value="Voter pour supprimer un point de racisme", inline=False)
        embedVar.add_field(name="$ajoute [nom]", value="Ajoute un raciste pas répertorié", inline=False)
        embedVar.add_field(name="$score [nom]", value="Vérifier le score", inline=False)
        embedVar.add_field(name="$racistes", value="Affiche tous les racistes", inline=False)
        embedVar.add_field(name="$reset", value="Reset tous les scores", inline=False)
        embedVar.add_field(name="$res [nom]", value="Reset quelqu'un", inline=False)
        embedVar.add_field(name="$droits", value="Verifier si t'as des droits en plus", inline=False)
        embedVar.add_field(name="$suppr [nom]", value="Supprimer un raciste", inline=False)
        embedVar.add_field(name="$amogos", value="Amogos", inline=False)
        await message.channel.send(embed=embedVar)
    
    if message.content.startswith('$racistes'):
        embedVar = discord.Embed(title="LES RACISTES", description="c mwa ", color=0x00ff00)
        for i in noms():
            embedVar.add_field(name=i[0].upper() + i[1:], value=check(i)[0], inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('$suppr '):
        nom = message.content.split()[1]
        if (check_admin(message.author.mention)):
            if del_person(nom) == 1:
                await message.channel.send(f"J'ai supprimé {nom[0].upper()}{nom[1:]} ♻")
            else:
                await message.channel.send(f"{nom[0].upper()}{nom[1:]} existe pas ♻")
        else:
            await message.channel.send("T'as pas les droits bg ❌")

    if message.content.startswith('$reset'):
        if (check_admin(message.author.mention)):
            reset()
            await message.channel.send("RESET TLMD ♻")
        else:
            await message.channel.send("T'as pas les droits bg ❌")

    if message.content.startswith('$amogos'):
        f = open("amogos.txt", "r")
        await message.channel.send(f.read())

    if message.content.startswith('$res '):
        nom = message.content.split()[1]
        if (check_admin(message.author.mention)):
            res(nom)
            await message.channel.send("RESET "+nom+" ♻")
        else:
            await message.channel.send("T'as pas les droits bg ❌")

    if message.content.startswith('$droits'):
        if (check_admin(message.author.mention)):
            await message.channel.send("Toi t'as les droits bg ✅")
        else:
            await message.channel.send("T'as pas les droits bg ❌")

client.run("Nzc4NjEzOTcyMzY1NjA2OTU0.X7UixA.4m1b6RupgdiBo5LJHjEEOaE17K8")