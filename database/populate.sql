INSERT INTO `categories` (`name`) VALUES ('Desserts');
INSERT INTO `categories` (`name`) VALUES ('Entrées');
INSERT INTO `categories` (`name`) VALUES ('Plats');

INSERT INTO `difficulty` (`label`) VALUES ('Facile');
INSERT INTO `difficulty` (`label`) VALUES ('Intermédiaire');
INSERT INTO `difficulty` (`label`) VALUES ('Difficile');

INSERT INTO `tools` (`name`) VALUES ('Mixeur');
INSERT INTO `tools` (`name`) VALUES ('Four');
INSERT INTO `tools` (`name`) VALUES ('Casserole');

INSERT INTO ingredients (name, unit) VALUES ('Sel', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Poivre', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Huile d\'olive', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Vinaigre balsamique', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Ail', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Oignon', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Persil', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Citron', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Tomate', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Concombre', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Carotte', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Céleri', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Pomme de terre', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Pain', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Pâte feuilletée', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Pâte brisée', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Pâte à pizza', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Fromage râpé', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Jambon', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Lait', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Crème fraîche', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Yaourt', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Fromage blanc', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Miel', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Sirop d\'érable', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Chocolat', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Cacao en poudre', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Cannelle', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Noix de muscade', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Poudre d\'amandes', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Noix', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Noisettes', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Amandes', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Pistaches', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Farine de blé', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Farine de maïs', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Sucre en poudre', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Sucre brun', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Sucre glace', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Levure de boulanger', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Levure sèche', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Levure chimique', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Piment', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Curry', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Moutarde', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Gingembre frais', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Cumin', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Coriandre', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Basilic', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Thym', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Origan', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Menthe', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Aneth', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Paprika', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Piment doux', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Curcuma', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Cardamome', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Clou de girofle', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Muscade', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Vanille', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Rhum', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Vin blanc', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Vin rouge', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Vin rosé', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Bières', 'unité');
INSERT INTO ingredients (name, unit) VALUES ('Whisky', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Vodka', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Rhum blanc', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Tequila', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Cognac', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Champagne', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Soda', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Eau gazeuse', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Eau plate', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Jus de citron', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Jus d\'orange', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Jus de pomme', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Jus de tomate', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Jus de fruits', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Jus de légumes', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Mayonnaise', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Ketchup', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Sauce soja', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Sauce Worcestershire', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Sauce piquante', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Sauce barbecue', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Sauce pesto', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Sauce tomate', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Sauce béchamel', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Sauce hollandaise', 'ml');
INSERT INTO ingredients (name, unit) VALUES ('Sauce tartare', 'g');
INSERT INTO ingredients (name, unit) VALUES ('Sauce aïoli', 'ml');

INSERT INTO `recipes` (`category_id`, `difficulty_id`, `cooker`, `name`, `picture`, `cooking_time_s`)
VALUES (1, 1, 'Eliott', 'Pâte ketchup', 'https://ds.static.rtbf.be/article/image/1920x1080/7/4/b/f38e49d28030c23aa18ad785e3b943a4-1631795947.jpg', 1800);

INSERT INTO `recipes` (`category_id`, `difficulty_id`, `cooker`, `name`, `picture`, `cooking_time_s`)
VALUES (2, 2, 'Mathéo', 'Courgette crue', 'https://resize.prod.docfr.doc-media.fr/s/1200/ext/eac4ff34/content/2022/7/5/courgette-8ae66ada146b1b74.jpeg', 2400);

INSERT INTO `recipes` (`category_id`, `difficulty_id`, `cooker`, `name`, `picture`, `cooking_time_s`)
VALUES (3, 3, 'Marianne', 'Riz', 'https://assets.afcdn.com/story/20230519/2219514_w3888h3888c1cx1944cy1400cxt0cyt0cxb3887cyb2592.jpg', 1500);

INSERT INTO `recipe_ingredient` (`id_recipe`, `id_ingredient`, `quantity`) VALUES (1, 1, 100);
INSERT INTO `recipe_ingredient` (`id_recipe`, `id_ingredient`, `quantity`) VALUES (1, 2, 50);

INSERT INTO `recipe_ingredient` (`id_recipe`, `id_ingredient`, `quantity`) VALUES (2, 3, 100);
INSERT INTO `recipe_ingredient` (`id_recipe`, `id_ingredient`, `quantity`) VALUES (2, 4, 50);

INSERT INTO `recipe_ingredient` (`id_recipe`, `id_ingredient`, `quantity`) VALUES (3, 2, 100);
INSERT INTO `recipe_ingredient` (`id_recipe`, `id_ingredient`, `quantity`) VALUES (3, 5, 50);

INSERT INTO `recipe_tool` (`id_recipe`, `id_tool`) VALUES (1, 1);
INSERT INTO `recipe_tool` (`id_recipe`, `id_tool`) VALUES (1, 2);

INSERT INTO `recipe_tool` (`id_recipe`, `id_tool`) VALUES (2, 2);
INSERT INTO `recipe_tool` (`id_recipe`, `id_tool`) VALUES (2, 3);

INSERT INTO `recipe_tool` (`id_recipe`, `id_tool`) VALUES (3, 1);
INSERT INTO `recipe_tool` (`id_recipe`, `id_tool`) VALUES (3, 3);

INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (1, 1, 'Etape 1', 'Mélanger les ingrédients');
INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (1, 3, 'Etape 3', 'Manger');
INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (1, 2, 'Etape 2', 'Mettre au four');

INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (2, 1, 'Etape 1', 'Couper la courgette');
INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (2, 2, 'Etape 2', 'Manger');

INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (3, 1, 'La base', "Mettre le riz dans l\'eau");
INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (3, 2, 'Ensuite...', 'Attendre environ 15 minutes, vous pouvez écouter de la musique en attendant');
INSERT INTO `steps` (`id_recipe`, `step_number`, `title`, `description`) VALUES (3, 3, 'Pour finir', "Il ne reste plus qu'a servir et à manger !");
