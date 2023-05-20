PRAGMA foreign_keys = ON;

--
-- Base de données : `imacook`
--

-- --------------------------------------------------------

--
-- Structure de la table `categories`
--

CREATE TABLE IF NOT EXISTS `categories` (
  `id` INTEGER PRIMARY KEY,
  `name` TEXT NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table `cookers`
--

CREATE TABLE IF NOT EXISTS `cookers` (
  `id` INTEGER PRIMARY KEY,
  `name` TEXT NOT NULL,
  `password` TEXT NOT NULL
);


-- --------------------------------------------------------

--
-- Structure de la table `difficulty`
--

CREATE TABLE IF NOT EXISTS `difficulty` (
  `id` INTEGER PRIMARY KEY,
  `label` TEXT NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table `ingredients`
--

CREATE TABLE IF NOT EXISTS `ingredients` (
  `id` INTEGER PRIMARY KEY,
  `name` TEXT NOT NULL,
  `unit` TEXT NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table `recipes`
--

CREATE TABLE IF NOT EXISTS `recipes` (
  `id` INTEGER PRIMARY KEY,
  `category_id` INTEGER NOT NULL,
  `difficulty_id` INTEGER NOT NULL,
  `cooker_id` INTEGER NOT NULL,
  `name` TEXT NOT NULL,
  `picture` TEXT NOT NULL,
  `cooking_time_s` INTEGER NOT NULL,
  FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  FOREIGN KEY (`cooker_id`) REFERENCES `cookers` (`id`),
  FOREIGN KEY (`difficulty_id`) REFERENCES `difficulty` (`id`)
);

-- --------------------------------------------------------

--
-- Structure de la table `recipe_ingredient`
--

CREATE TABLE IF NOT EXISTS `recipe_ingredient` (
  `id_recipe` INTEGER NOT NULL,
  `id_ingredient` INTEGER NOT NULL,
  `quantity` INTEGER NOT NULL,
  FOREIGN KEY (`id_recipe`) REFERENCES `recipes` (`id`),
  FOREIGN KEY (`id_ingredient`) REFERENCES `ingredients` (`id`)
);

-- --------------------------------------------------------

--
-- Structure de la table `recipe_tool`
--

CREATE TABLE IF NOT EXISTS `recipe_tool` (
  `id_recipe` INTEGER NOT NULL,
  `id_tool` INTEGER NOT NULL,
  FOREIGN KEY (`id_recipe`) REFERENCES `recipes` (`id`),
  FOREIGN KEY (`id_tool`) REFERENCES `tools` (`id`)
);

-- --------------------------------------------------------

--
-- Structure de la table `steps`
--

CREATE TABLE IF NOT EXISTS `steps` (
  `id` INTEGER PRIMARY KEY,
  `id_recipe` INTEGER NOT NULL,
  `step_number` INTEGER NOT NULL,
  `title` TEXT NOT NULL,
  `description` TEXT NOT NULL,
  FOREIGN KEY (`id_recipe`) REFERENCES `recipes` (`id`)
);

-- --------------------------------------------------------

--
-- Structure de la table `tools`
--

CREATE TABLE IF NOT EXISTS `tools` (
  `id` INTEGER PRIMARY KEY,
  `name` TEXT NOT NULL
);