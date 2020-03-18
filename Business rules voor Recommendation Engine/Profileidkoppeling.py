"""
select profiles.id, profiles.latestactivity, sessions.duration, profiles_previously_viewed.prodid, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from profiles
right JOIN sessions ON profiles.id=sessions.profid
right JOIN profiles_previously_viewed ON profiles.id=profiles_previously_viewed.profid
right JOIN products ON products.id=profiles_previously_viewed.prodid
select products.id, products.category, products.subcategory, products.targetaudience, products.sellingprice, products.deal from products WHERE products.deal IS NOT NULL and products.category is not null
order by category, subcategory, targetaudience,deal asc
"""