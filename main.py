import discord
import os
import json

client = discord.Client()

def add_person(nom):
    nom = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    if nom not in lis:
        lis[nom] = [0, 0]
    else:
        return (-1)
    with open('save.txt', 'w') as convert_file:
     convert_file.write(json.dumps(lis))

def add_raciste(nom):
    nom = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    if nom in lis:
        lis[nom] = [lis[nom][0] + 1, lis[nom][1] + 1]
    else:
        return (-1)
    with open('save.txt', 'w') as convert_file:
     convert_file.write(json.dumps(lis))

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
        lis[i] = [0, 0]
    with open('save.txt', 'w') as convert_file:
     convert_file.write(json.dumps(lis))

def res(nom):
    nom = nom.lower()
    with open('save.txt') as f:
        data = f.read()
    lis = json.loads(data)
    lis[nom] = [0, 0]
    with open('save.txt', 'w') as convert_file:
     convert_file.write(json.dumps(lis))

@client.event
async def on_ready():
    print('Wesh {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$raciste '):
        nom = message.content.split()[1]
        if add_raciste(nom) == -1:
            await message.channel.send(f"{nom[0].upper()}{nom[1:]} est pas encore raciste, rajoute le avec '$ajoute {nom}'!")
        else:
            await message.channel.send(f"Pitin de raciste {nom} +1 !")
    
    if message.content.startswith('$ajoute '):
        nom = message.content.split()[1]
        if add_person(nom) == -1:
            await message.channel.send(f"{nom[0].upper()}{nom[1:]} existe deja ce raciste...")
        else:
            await message.channel.send(f"J'ai ajouté {nom} ce raciste!")
    
    if message.content.startswith('$score '):
        nom = message.content.split()[1]
        embedVar = discord.Embed(title="SCORE", description="Raciste ?? "+nom, color=0x00ff00)
        embedVar.add_field(name="Depuis toujours", value=check(nom)[0], inline=False)
        embedVar.add_field(name="Cette semaine", value=check(nom)[1], inline=False)
        if check(nom) == "-1":
            await message.channel.send(f"{nom[0].upper()}{nom[1:]} existe pas ce raciste...")
        else:
            await message.channel.send(embed=embedVar)
    
    if message.content.startswith('$commandes') or message.content.startswith('$help'):
        embedVar = discord.Embed(title="Commandes", description="$", color=0x00ff00)
        embedVar.add_field(name="$raciste [nom]", value="Ajouter un point de racisme", inline=False)
        embedVar.add_field(name="$ajoute [nom]", value="Ajoute un raciste pas répertorié", inline=False)
        embedVar.add_field(name="$score [nom]", value="Vérifier le score", inline=False)
        embedVar.add_field(name="$racistes", value="Affiche tous les racistes", inline=False)
        embedVar.add_field(name="$reset", value="Reset tous les scores", inline=False)
        embedVar.add_field(name="$res [nom]", value="Reset quelqu'un", inline=False)
        await message.channel.send(embed=embedVar)
    
    if message.content.startswith('$racistes'):
        embedVar = discord.Embed(title="LES RACISTES", description="c mwa ", color=0x00ff00)
        for i in noms():
            embedVar.add_field(name=i[0].upper() + i[1:], value=check(i)[0], inline=False)
        await message.channel.send(embed=embedVar)

    if message.content.startswith('$reset'):
        reset()
        await message.channel.send("RESET")

    if message.content.startswith('$res '):
        nom = message.content.split()[1]
        res(nom)
        await message.channel.send("Reset "+nom)

client.run("Nzc4NjEzOTcyMzY1NjA2OTU0.X7UixA.4m1b6RupgdiBo5LJHjEEOaE17K8")