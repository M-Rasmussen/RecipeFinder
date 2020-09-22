import sys
import os
import flask
import random
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import tweepy

''' class of recipie to hold the information'''
class Recipes:
    def __init__(self,name,pic,inregients,instructions):
    	self.name=name
    	self.pic=pic
    	self.inregients=inregients
    	self.instructions=instructions


cake_name="Cake"
cake_picture= "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2012/12/20/2/FNM_010113-Basic-Vanilla_s4x3.jpg.rend.hgtvcom.826.620.suffix/1371613590018.jpeg"
cake_inregient= ["2 sticks unsalted butter, at room temperature, plus more for the pans", "3 cups all-purpose flour, plus more for the pans", "1 tablespoon baking powder","1/2 teaspoon salt","1 1/4 cups sugar", "4 large eggs, at room temperature", "1 tablespoon vanilla extract", "1 1/4 cups whole milk (or 3/4 cup heavy cream mixed with 1/2 cup water)"]
cake_instruction=["Preheat the oven to 350 degrees F. Butter two 9-inch-round cake pans and line the bottoms with parchment paper; butter the parchment and dust the pans with flour, tapping out the excess.", "Whisk 3 cups flour, the baking powder and salt in a bowl until combined. Beat 2 sticks butter and the sugar in a large bowl with a mixer on medium-high speed until light and fluffy, about 3 minutes. Reduce the mixer speed to medium; beat in the eggs, one at a time, scraping down the bowl as needed. Beat in the vanilla. (The mixture may look separated at this point.) Beat in the flour mixture in 3 batches, alternating with the milk, beginning and ending with flour, until just smooth.", "Divide the batter between the prepared pans. Bake until the cakes are lightly golden on top and a toothpick inserted into the middle comes out clean, 30 to 35 minutes. Transfer to racks and let cool 10 minutes, then run a knife around the edge of the pans and turn the cakes out onto the racks to cool completely. Remove the parchment. Trim the tops of the cakes with a long serrated knife to make them level, if desired."]
cake_website="https://www.foodnetwork.com/recipes/food-network-kitchen/basic-vanilla-cake-recipe-2043654"

waffle_name="Waffles"
waffle_picture="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fassets.marthastewart.com%2Fstyles%2Fwmax-300%2Fd19%2Fmsledf_1105_waffles%2Fmsledf_1105_waffles_vert.jpg%3Fitok%3D83ZYPjni"
waffle_inregient=["1 cup all-purpose flour, spooned and leveled","2 tablespoons sugar", "1 teaspoon baking powder","1/4 teaspoon salt","1 cup milk","2 large eggs","4 tablespoons (1/2 stick) unsalted butter, melted","Maple syrup and butter, as desired, for serving" ]
waffle_instruction=["Preheat waffle iron according to manufacturer's instructions. In a large bowl, whisk flour, sugar, baking powder, and salt; set aside.","In a small bowl, whisk milk and eggs; pour over flour mixture, and whisk gently to combine (don't overmix). Gently whisk in butter.", "Following manufacturer's instructions, cook waffles until deep brown and crisp. (For a standard waffle iron, pour a generous 1/2 cup of batter into center, spreading to within 1/2 inch of edges, and close; waffle will cook in 2 to 3 minutes.) Serve warm, with maple syrup and butter, as desired."]
Waffles_website="https://www.marthastewart.com/338522/waffles"

pbj_name="PBJ"
pbj_picture="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/flapjack-651d314.jpg?quality=90&webp=true&resize=300,272"
pbj_inregient=["5 tbsp salted butter , plus extra for the tin", "250g crunchy peanut butter", "8 tbsp strawberry or raspberry jam", "80g light brown soft sugar", "200g rolled oats"]
pbj_instruction=["Heat the oven to 180C/160C fan/gas 4. Butter and line the base and sides of a 20cm square cake tin with baking parchment.", "Put 3 tbsp each of the peanut butter and jam in separate small bowls and set aside. Tip the remaining peanut butter, the rest of the jam and the butter and sugar into a pan set over a medium heat and stir until everything has melted together. Quickly stir in the oats, then leave to cool for 5 mins.","Spoon the mixture into the prepared cake tin and gently press down with your hands. Dot over the reserved peanut butter and jam, then bake for 20-25 mins or until golden brown. Leave to cool completely in the tin, then turn out onto a board and cut into squares."]
pbj_website="https://www.bbcgoodfood.com/recipes/peanut-butter-and-jam-flapjacks"

pizza_name="Pizza"
pizza_picture="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/delish-homemade-pizza-horizontal-1542312378.png?crop=1.00xw:1.00xh;0,0&resize=980:*"
pizza_inregient=["1 package (1/4 ounce) active dry yeast","1 teaspoon sugar","1-1/4 cups warm water (110° to 115°)", "1/4 cup canola oil", "1 teaspoon salt", "3-1/2 to 4 cups all-purpose flour", "1/2 pound ground beef", "1 small onion, chopped", "1 can (15 ounces) tomato sauce", "3 teaspoons dried oregano", "1 teaspoon dried basil", "1 medium green pepper, diced", "2 cups shredded part-skim mozzarella cheese"]
pizza_instruction=["In large bowl, dissolve yeast and sugar in water; let stand for 5 minutes. Add oil and salt. Stir in flour, 1 cup at a time, until a soft dough forms.", "Turn onto floured surface; knead until smooth and elastic, 2-3 minutes. Place in a greased bowl, turning once to grease the top. Cover and let rise in a warm place until doubled, about 45 minutes. Meanwhile, cook beef and onion over medium heat until no longer pink; drain.", "Punch down dough; divide in half. Press each into a greased 12-in. pizza pan. Combine the tomato sauce, oregano and basil; spread over each crust. Top with beef mixture, green pepper and cheese.", "Bake at 400° for 25-30 minutes or until crust is lightly browned."]
pizza_website="https://www.tasteofhome.com/recipes/homemade-pizza/"

doughnuts_name="Doughnuts"
doughnuts_picture="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F447823.jpg&w=596&h=596&c=sc&poi=face&q=85"
doughnuts_inregient=["2 cups all-purpose flour","1/2 cup white sugar","1 teaspoon salt","1 tablespoon baking powder","1/4 teaspoon ground cinnamon","1 dash ground nutmeg","2 tablespoons melted butter","1/2 cup milk","1 egg, beaten","1 quart oil for frying"]
doughnuts_instruction=["Heat oil in deep-fryer to 375 degrees F (190 degrees C).", "In a large bowl, sift together flour, sugar, salt, baking powder, cinnamon and nutmeg. Mix in butter until crumbly. Stir in milk and egg until smooth. Knead lightly, then turn out onto a lightly floured surface. Roll or pat to 1/4 inch thickness. Cut with a doughnut cutter, or use two round biscuit cutters of different sizes.", "Carefully drop doughnuts into hot oil, a few at a time. Do not overcrowd pan or oil may overflow. Fry, turning once, for 3 minutes or until golden. Drain on paper towels."]
doughnuts_website="https://www.allrecipes.com/recipe/43051/plain-cake-doughnuts/"

cookie_name="Cookies"
cookie_picture="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5960754.jpg&w=596&h=596&c=sc&poi=face&q=85"
cookie_inregient=["1 cup butter, softened","1 cup white sugar","1 cup packed brown sugar","2 large eggs","2 teaspoons vanilla extract","1 teaspoon baking soda","2 teaspoons hot water","1/2 teaspoon salt","3 cups all-purpose flour","2 cups semisweet chocolate chips","1 cup chopped walnuts"]
cookie_instruction=["Preheat oven to 350 degrees F (175 degrees C).", "Cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.", "Bake for about 10 minutes in the preheated oven, or until edges are nicely browned."]
cookie_website="https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/"

pump_name="Pumpkin Bread"
pump_picture="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4540321.jpg&w=595&h=398&c=sc&poi=face&q=85"
pump_inregient=["1 (15 ounce) can pumpkin pure","4 large eggs eggs","1 cup vegetable oil","2/3 cup water","3 cups white sugar","3 1/2 cups all-purpose flour","2 teaspoons baking soda","1 1/2 teaspoons salt","1 teaspoon ground cinnamon","1 teaspoon ground nutmeg","1/2 teaspoon ground cloves","1/4 teaspoon ground ginger"]
pump_instruction=["Preheat oven to 350 degrees F (175 degrees C). Grease and flour three 7x3 inch loaf pans.","In a large bowl, mix together pumpkin puree, eggs, oil, water and sugar until well blended. In a separate bowl, whisk together the flour, baking soda, salt, cinnamon, nutmeg, cloves and ginger. Stir the dry ingredients into the pumpkin mixture until just blended. Pour into the prepared pans.","Bake for about 50 minutes in the preheated oven. Loaves are done when toothpick inserted in center comes out clean."]
pump_website="https://www.allrecipes.com/recipe/6820/downeast-maine-pumpkin-bread/"

cake = Recipes(cake_name, cake_picture,cake_inregient,cake_instruction)
waffle= Recipes(waffle_name, waffle_picture, waffle_inregient, waffle_instruction)
pbj = Recipes(pbj_name, pbj_picture, pbj_inregient, pbj_instruction)
pizza= Recipes(pizza_name, pizza_picture, pizza_inregient, pizza_instruction)
doughnuts=Recipes(doughnuts_name, doughnuts_picture, doughnuts_inregient,doughnuts_instruction)
cookie=Recipes(cookie_name, cookie_picture, cookie_inregient, cookie_instruction)
pumpkinBread=Recipes(pump_name, pump_picture, pump_inregient, pump_instruction)

RecipesList=[cake, waffle, pbj, pizza, doughnuts, cookie, pumpkinBread]

ranNumb=random.randint(0,6)


twitter_consumer_key=os.environ['TWIITER_CONSUMER_KEY']
twitter_consumer_secret=os.environ['TWITTER_CONSUMER_SECRET']
twitter_access_token=os.environ['TWITTER_ACCESS_TOKEN']
twitter_access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)
auth_api = API(auth)

date_since = "2018-11-16"
tweets=tweepy.Cursor(auth_api.search, q="#"+RecipesList[ranNumb].name, lang="en",since=date_since).items(1)
for tweet in tweets:
    tweetText=tweet.text
    tweetUserName=tweet.user.screen_name
    tweetDate=tweet.created_at
app = flask.Flask(__name__)

@app.route("/") # "Python decorator"
def index():
    return flask.render_template("index.html", iName = RecipesList[ranNumb].name, iPic = RecipesList[ranNumb].pic, iIngredients=RecipesList[ranNumb].inregients, iInstructions=RecipesList[ranNumb].instructions, tweeterName=tweetUserName, tweeterText=tweetText, tweeterDate=tweetDate)
    
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
