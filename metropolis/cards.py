from metropolis.MetropolisCard import MetropolisCard as card
from metropolis.MetropolisExtraInfo import MetropolisExtraInfo
from metropolis.MetropolisSign import signs as s, MetropolisSign as sgn
from metropolis.incpntfuncs import constant as c, per_sign as ps, with_card as wc, stadsvilla_pts as sv,\
    metro_ppr as mpr, in_game as ig, per_card_in_game as pc

# signs: source, shop, car
no_signs = s(0, 0, 0)

# extra infos (more at the bottom)
max_1pp = MetropolisExtraInfo("max. 1/speler", max_amount=1)
bouwkeet_description = "Je mag elke ronde 2 gebouwen bouwen\ndie elk niet meer dan 4 (vóór kortingen)\n" +\
                       "kosten (inclusief een tweede gebouw\nin de ronde dat je deze kaart bouwt)"

# cards
architect = card("Architect", 0, no_signs, c(1), c(0), max_1pp)
zakencentrum = card("Zakencentrum", 3, s(2, 0, 0), c(1), c(1))
beursgebouw = card("Beursgebouw", 3, s(0, 0, 1), c(1), c(1))
school = card("School", 1, no_signs, c(0), c(2))
rijtjeshuis = card("Rijtjeshuis", 1, s(1, 0, 0), c(0), c(1))
winkelstraat = card("Winkelstraat", 1, s(0, 1, 1), c(1), c(0))
klaverblad = card("Klaverblad", 2, s(0, 0, 0), ps(1, sgn.CAR), ps(1, sgn.CAR), max_1pp)
monument = card("Monument", 9, s(3, 0, 0), c(1), c(8))
casino = card("Casino", 6, s(0, 1, 0), c(4), c(1))
universiteit = card("Universiteit", 5, s(1, 0, 0), c(0), pc(4, 1, school))
onderzoekscentrum = card("Onderzoekscentrum", 4, no_signs, c(1), ig(2, 2, universiteit))
ziekenhuis = card("Ziekenhuis", 6, s(1, 0, 0), c(1), c(4))
kantoorgebouw = card("Kantoorgebouw", 2, no_signs, wc(1, 1, rijtjeshuis), c(2))
pretpark = card("Pretpark", 8, s(0, 0, 3), c(2), c(5))
bioscoopcomplex = card("Bioscoopcomplex", 4, s(0, 2, 1), c(2), c(1))
technopark = card("Technopark", 5, s(1, 0, 1), c(2), c(2))
operagebouw = card("Operagebouw", 8, s(1, 0, 0), c(0), c(8))
concertgebouw = card("Concertgebouw", 7, s(1, 0, 0), c(0), c(7))
busstation = card("Busstation", 1, s(1, 1, 0), wc(0, 1, winkelstraat), c(1))
superstore = card("Superstore", 6, s(0, 2, 1), c(3), c(1))
bouwkeet = card("Bouwkeet", 1, no_signs, c(0), c(0), MetropolisExtraInfo(bouwkeet_description, builds_per_turn=2))
sportpark = card("Sportpark", 4, s(0, 0, 2), c(0), c(3))
theater = card("Theater", 5, s(1, 0, 0), c(1), c(3))
metro = card("Metro", 11, no_signs, c(0), mpr(1, 1, sgn.SOURCE, sgn.SOURCE))
museum = card("Museum", 5, s(1, 0, 0), pc(0, 2, school), c(4))
stadhuis = card("Stadhuis", 6, s(1, 0, 0), c(0), c(5))
woonwijk = card("Woonwijk", 1, s(0, 1, 1), c(0), c(1))
stadion = card("Stadion", 6, s(0, 0, 2), c(2), c(3))
warenhuis = card("Warenhuis", 3, s(1, 1, 0), c(2), c(0))
park = card("Park", 1, s(1, 0, 0), c(0), ps(1, sgn.SOURCE), max_1pp)
bioscoop = card("Bioscoop", 2, s(1, 1, 1), c(1), c(0))
treinstation = card("Treinstation", 4, s(1, 1, 1), c(1), c(2))
vliegveld = card("Vliegveld", 9, s(0, 1, 1), c(1), c(8))
industriepark = card("Industriepark", 1, no_signs, wc(1, 1, onderzoekscentrum), c(0))
parkeerplusreis = card("Parkeer + Reis", 11, s(0, 0, 2), c(0), mpr(1, 1, sgn.CAR, sgn.CAR))
snelweg = card("Snelweg", 3, s(0, 0, 1), c(0), pc(0, 2, klaverblad))
parkeergarage = card("Parkeergarage", 0, s(1, 1, 1), c(0), c(0))
congrescentrum = card("Congrescentrum", 7, s(1, 1, 0), c(1), c(5))
handelscentrum = card("Handelscentrum", 7, s(0, 3, 0), c(2), ps(1, sgn.SHOP))
winkelpassage = card("Winkelpassage", 2, s(0, 1, 1), ps(1, sgn.SHOP), c(0), max_1pp)
restaurant = card("Restaurant", 1, s(1, 1, 0), wc(0, 1, zakencentrum), c(1))
industrieterrein = card("Industrieterrein", 2, s(0, 0, 1), c(1), c(0))
gemeentehuis = card("Gemeentehuis", 2, no_signs, ps(1, sgn.SOURCE), c(1))
modernekunst = card("Moderne kunst", 4, s(2, 0, 0), c(0), c(3))
woonhuis = card("Woonhuis", 1, no_signs, c(1), c(0))
brug = card("Brug", 4, s(0, 0, 1), wc(1, 1, snelweg), c(2))
fake_stadsvilla = card("Stadsvilla", 55, no_signs, c(0), c(0))
stadsvilla = card("Stadsvilla", 4, no_signs, c(0), sv(3, 2, fake_stadsvilla))
flatgebouw = card("Flatgebouw", 3, s(1, 1, 0), c(1), c(1))
modeboetiek = card("Modeboetiek", 2, s(1, 1, 0), wc(1, 1, zakencentrum), c(0))
wolkenkrabber = card("Wolkenkrabber", 8, s(1, 0, 0), c(1), c(7))


all_cards = [architect, zakencentrum, beursgebouw, school, rijtjeshuis, winkelstraat, klaverblad, monument, casino,
             universiteit, onderzoekscentrum, ziekenhuis, kantoorgebouw, pretpark, bioscoopcomplex, technopark,
             operagebouw, concertgebouw, busstation, superstore, bouwkeet, sportpark, theater, metro, museum, stadhuis,
             woonwijk, stadion, warenhuis, park, bioscoop, treinstation, vliegveld, industriepark, parkeerplusreis,
             snelweg, parkeergarage, congrescentrum, handelscentrum, winkelpassage, restaurant, industrieterrein,
             gemeentehuis, modernekunst, woonhuis, brug, stadsvilla, flatgebouw, modeboetiek, wolkenkrabber]

# extra infos (max. 1pp + bouwkeet already done above)
# gemeentehuis
src_discounts = {}
for card in all_cards:
    if card.num_signs[sgn.SOURCE] >= 1:
        src_discounts[card] = 1
gemeentehuis.extra_info = MetropolisExtraInfo(f"max. 1/speler\n-1 bouwkosten voor alle kaarten met {sgn.SOURCE}",
                                              max_amount=1, discounts=src_discounts)
winkelstraat.extra_info = MetropolisExtraInfo(f"Voorwaarde:\n{woonhuis} of {woonwijk}\n of {klaverblad}",
                                              needs=[woonhuis, woonwijk, klaverblad])
kantoorgebouw.extra_info = MetropolisExtraInfo(f"Voorwaarde:\n{woonhuis} of {woonwijk} of\n{rijtjeshuis} of {flatgebouw}",
                                              needs=[woonhuis, woonwijk, rijtjeshuis, flatgebouw])
school.extra_info = MetropolisExtraInfo(f"Voorwaarde:\n{woonhuis} of {woonwijk} of {stadsvilla}\n" +
                                        f"-2 bouwkosten voor {stadsvilla}\n als je ten minste 1 {school} hebt",
                                        needs=[woonhuis, woonwijk, stadsvilla], discounts={stadsvilla: 2})
industriepark.extra_info = MetropolisExtraInfo(f"-1 bouwkosten voor {onderzoekscentrum}\n" +
                                               f" en {industrieterrein} als je \nten minste 1 {industriepark} hebt",
                                               discounts={onderzoekscentrum: 1, industrieterrein: 1})
industrieterrein.extra_info = MetropolisExtraInfo(f"-1 bouwkosten voor {snelweg}\n" +
                                                  f" en {klaverblad} als je \nten minste 1 {industrieterrein} hebt",
                                                  discounts={snelweg: 1, klaverblad: 1})
onderzoekscentrum.extra_info = MetropolisExtraInfo(f"-2 bouwkosten voor {technopark}\n" +
                                                   f" en {ziekenhuis} als je \nten minste 1 {onderzoekscentrum} hebt",
                                                   discounts={technopark: 2, ziekenhuis: 2})
rijtjeshuis.extra_info = MetropolisExtraInfo(f"-1 bouwkosten voor {restaurant}\n" +
                                             f" en {modeboetiek} als je \nten minste 1 {rijtjeshuis} hebt",
                                             discounts={restaurant: 1, modeboetiek: 1})
