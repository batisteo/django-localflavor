# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#: See the "Code officiel géographique" on the INSEE website <www.insee.fr>.
REGION_CHOICES = (
    # Overseas regions
    ('01', 'Guadeloupe'),
    ('02', 'Martinique'),
    ('03', 'Guyane'),
    ('04', 'La Réunion'),
    ('05', 'Mayotte'),
    # Metropolitan regions
    ('11', 'Île-de-France'),
    ('21', 'Champagne-Ardenne'),
    ('22', 'Picardie'),
    ('23', 'Haute-Normandie'),
    ('24', 'Centre'),
    ('25', 'Basse-Normandie'),
    ('26', 'Bourgogne'),
    ('31', 'Nord-Pas-de-Calais'),
    ('41', 'Lorraine'),
    ('42', 'Alsace'),
    ('43', 'Franche-Comté'),
    ('52', 'Pays de la Loire'),
    ('53', 'Bretagne'),
    ('54', 'Poitou-Charentes'),
    ('72', 'Aquitaine'),
    ('73', 'Midi-Pyrénées'),
    ('74', 'Limousin'),
    ('82', 'Rhône-Alpes'),
    ('83', 'Auvergne'),
    ('91', 'Languedoc-Roussillon'),
    ('93', 'Provence-Alpes-Côte d\'Azur'),
    ('94', 'Corse')
)

#: France changed its regions in 2016 (see http://www.insee.fr/fr/methodes/nomenclatures/cog/)
NEW_REGION_CHOICES = (
    # Overseas regions
    ('01', "Guadeloupe"),
    ('02', "Martinique"),
    ('03', "Guyane"),
    ('04', "La Réunion"),
    ('06', "Mayotte"),
    # Metropolitan regions
    ('11', "Île-de-France"),
    ('24', "Centre-Val de Loire"),
    ('27', "Bourgogne-Franche-Comté"),
    ('28', "Normandie"),
    ('32', "Nord-Pas-de-Calais-Picardie"),
    ('44', "Alsace-Champagne-Ardenne-Lorraine"),
    ('52', "Pays de la Loire"),
    ('53', "Bretagne"),
    ('75', "Aquitaine-Limousin-Poitou-Charentes"),
    ('76', "Languedoc-Roussillon-Midi-Pyrénées"),
    ('84', "Auvergne-Rhône-Alpes"),
    ('93', "Provence-Alpes-Côte d'Azur"),
    ('94', "Corse"),
)
