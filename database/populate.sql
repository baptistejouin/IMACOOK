INSERT INTO `cookers` (`name`, `password`) VALUES ('Eliott', 'mypassword');
INSERT INTO `cookers` (`name`, `password`) VALUES ('Mathéo', 'mypassword');
INSERT INTO `cookers` (`name`, `password`) VALUES ('Coralie', 'mypassword');

INSERT INTO `categories` (`name`) VALUES ('Desserts');
INSERT INTO `categories` (`name`) VALUES ('Entrées');
INSERT INTO `categories` (`name`) VALUES ('Plats');

INSERT INTO `difficulty` (`label`) VALUES ('Facile');
INSERT INTO `difficulty` (`label`) VALUES ('Intermédiaire');
INSERT INTO `difficulty` (`label`) VALUES ('Difficile');

INSERT INTO `tools` (`name`) VALUES ('Mixeur');
INSERT INTO `tools` (`name`) VALUES ('Four');
INSERT INTO `tools` (`name`) VALUES ('Casserole');

INSERT INTO `ingredients` (`name`, `unit`) VALUES ('Farine', 'g');
INSERT INTO `ingredients` (`name`, `unit`) VALUES ('Sucre', 'g');
INSERT INTO `ingredients` (`name`, `unit`) VALUES ('Beurre', 'g');
INSERT INTO `ingredients` (`name`, `unit`) VALUES ('Oeufs', 'unité');
INSERT INTO `ingredients` (`name`, `unit`) VALUES ('Levure chimique', 'g');

INSERT INTO `recipes` (`category_id`, `difficulty_id`, `cooker_id`, `name`, `picture`, `cooking_time_s`)
VALUES (1, 1, 1, 'Pâte ketchup', 'https://ds.static.rtbf.be/article/image/1920x1080/7/4/b/f38e49d28030c23aa18ad785e3b943a4-1631795947.jpg', 1800);

INSERT INTO `recipes` (`category_id`, `difficulty_id`, `cooker_id`, `name`, `picture`, `cooking_time_s`)
VALUES (2, 2, 2, 'Courgette crue', 'https://resize.prod.docfr.doc-media.fr/s/1200/ext/eac4ff34/content/2022/7/5/courgette-8ae66ada146b1b74.jpeg', 2400);

INSERT INTO `recipes` (`category_id`, `difficulty_id`, `cooker_id`, `name`, `picture`, `cooking_time_s`)
VALUES (3, 3, 3, 'Riz', 'https://assets.afcdn.com/story/20230519/2219514_w3888h3888c1cx1944cy1400cxt0cyt0cxb3887cyb2592.jpg', 1500);

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