def trouver_note_max_min(notes):
    note_max = max(notes)
    note_min = min(notes)
    return note_max, note_min

# Liste des notes des étudiants
notes_etudiants = [85, 92, 78, 65, 90, 87]

# Trouver la note la plus haute et la note la plus basse
note_max, note_min = trouver_note_max_min(notes_etudiants)

# Affichage des résultats
print("La note la plus haute est :", note_max)
print("La note la plus basse est :", note_min)
