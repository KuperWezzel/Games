from metropolis.MetropolisCard import MetropolisCard as card
from metropolis.MetropolisSign import signs as s, MetropolisSign as sgn
from metropolis.incpntfuncs import constant as c, per_sign as ps, with_card as wc, stadsvilla_pts as sv,\
    metro_ppr as mpr, in_game as ig, per_card_in_game as pc

# signs: source, shop, car
no_signs = s(0, 0, 0)

# cards
architect = card("Architect", 0, no_signs, c(1), c(0))
zakencentrum = card("Zakencentrum", 3, s(2, 0, 0), c(1), c(1))
beursgebouw = card("Beursgebouw", 3, s(0, 0, 1), c(1), c(1))
school = card("School", 1, no_signs, c(0), c(2))
rijtjeshuis = card("Rijtjeshuis", 1, s(1, 0, 0), c(0), c(1))
winkelstraat = card("Winkelstraat", 1, s(0, 1, 1), c(1), c(0))
klaverblad = card("Klaverblad", 2, s(0, 0, 0), ps(1, sgn.CAR), ps(1, sgn.CAR))
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
bouwkeet = card("Bouwkeet", 1, no_signs, c(0), c(0))
sportpark = card("Sportpark", 4, s(0, 0, 2), c(0), c(3))
theater = card("Theater", 5, s(1, 0, 0), c(1), c(3))
metro = card("Metro", 11, no_signs, c(0), mpr(1, 1, sgn.SOURCE, sgn.SOURCE))
museum = card("Museum", 5, s(1, 0, 0), pc(0, 2, school), c(4))
stadhuis = card("Stadhuis", 6, s(1, 0, 0), c(0), c(5))
woonwijk = card("Woonwijk", 1, s(0, 1, 1), c(0), c(1))
stadion = card("Stadion", 6, s(0, 0, 2), c(2), c(3))
warenhuis = card("Warenhuis", 3, s(1, 1, 0), c(2), c(0))
park = card("Park", 1, s(1, 0, 0), c(0), ps(1, sgn.SOURCE))
bioscoop = card("Bioscoop", 2, s(1, 1, 1), c(1), c(0))
treinstation = card("Treinstation", 4, s(1, 1, 1), c(1), c(2))
vliegveld = card("Vliegveld", 9, s(0, 1, 1), c(1), c(8))
industriepark = card("Industriepark", 1, no_signs, wc(1, 1, onderzoekscentrum), c(0))
parkeerplusreis = card("Parkeer + Reis", 11, s(0, 0, 2), c(0), mpr(1, 1, sgn.CAR, sgn.CAR))
snelweg = card("Snelweg", 3, s(0, 0, 1), c(0), pc(0, 2, klaverblad))
parkeergarage = card("Parkeergarage", 0, s(1, 1, 1), c(0), c(0))
congrescentrum = card("Congrescentrum", 7, s(1, 1, 0), c(1), c(5))
handelscentrum = card("Handelscentrum", 7, s(0, 3, 0), c(2), ps(1, sgn.SHOP))
winkelpassage = card("Winkelpassage", 2, s(0, 1, 1), ps(1, sgn.SHOP), c(0))
restaurant = card("Restaurant", 1, s(1, 1, 0), wc(0, 1, zakencentrum), c(1))
industrieterrein = card("Industrieterrein", 2, s(0, 0, 1), c(1), c(0))
gemeentehuis = card("Gemeentehuis", 2, no_signs, ps(1, sgn.SOURCE), c(1))
modernekunst = card("Moderne kunst", 4, s(2, 0, 0), c(0), c(3))
woonhuis = card("Woonhuis", 1, no_signs, c(1), c(0))
brug = card("Brug", 4, s(0, 0, 1), wc(1, 1, snelweg), c(2))
fake_stadsvilla = card("Stadsvilla", 55, no_signs, c(0), c(0))
stadsvilla = card("Stadvilla", 4, no_signs, c(0), sv(3, 2, fake_stadsvilla))
flatgebouw = card("Flatgebouw", 3, s(1, 1, 0), c(1), c(1))
modeboetiek = card("Modeboetiek", 2, s(1, 1, 0), wc(1, 1, zakencentrum), c(0))
wolkenkrabber = card("Wolkenkrabber", 8, s(1, 0, 0), c(1), c(7))


all_cards = [architect, zakencentrum, beursgebouw, school, rijtjeshuis, winkelstraat, klaverblad, monument, casino,
             universiteit, onderzoekscentrum, ziekenhuis, kantoorgebouw, pretpark, bioscoopcomplex, technopark,
             operagebouw, concertgebouw, busstation, superstore, bouwkeet, sportpark, theater, metro, museum, stadhuis,
             woonwijk, stadion, warenhuis, park, bioscoop, treinstation, vliegveld, industriepark, parkeerplusreis,
             snelweg, parkeergarage, congrescentrum, handelscentrum, winkelpassage, restaurant, industrieterrein,
             gemeentehuis, modernekunst, woonhuis, brug, stadsvilla, flatgebouw, modeboetiek, wolkenkrabber]
