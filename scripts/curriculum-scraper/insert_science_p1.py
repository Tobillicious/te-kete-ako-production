#!/usr/bin/env python3
"""
Science Phase 1 (Years 0-3) Manual Insertion Script
Systematically extracted from browser snapshot of Tahurangi.

Structure:
- Physical Science
  - Materials
  - Matter Interactions and Energy
  - Motion and Forces
  - Earth and Space
- Biological Science
  - Organism Diversity
  - Body Systems
  - Ecosystems
"""

# This will be executed via MCP tools, so we'll generate clean SQL

statements = []

# =====================
# PHYSICAL SCIENCE
# =====================

# MATERIALS - Year 1 Knowledge
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Materials",
    "sub_strand": "Materials and their properties",
    "element": "Knowledge",
    "year_levels": [1],
    "statements": [
        "Objects are made of different materials.",
        "Materials can be combined to make objects.",
        "Materials have observable properties (e.g. shape, texture, colour, hardness, flexibility).",
        "Soils and rocks have different properties, including firmness, texture, colour, and heaviness."
    ]
})

# MATERIALS - Year 2 Knowledge
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Materials",
    "sub_strand": "Material properties and uses",
    "element": "Knowledge",
    "year_levels": [2],
    "statements": [
        "Materials take up space and have mass.",
        "Mass is the amount of matter present in an object.",
        "Flexible materials can be bent.",
        "Elastic materials can be stretched or bent and returned to their original shape.",
        "Some elastic materials can return to their original shape faster than others.",
        "Materials can be cut, broken, and worn down into smaller fragments. These smaller parts remain (e.g. sand, breadcrumbs, glass shards).",
        "Materials can be natural or manufactured (made by humans)."
    ]
})

# MATERIALS - Year 1 Practices
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Materials",
    "sub_strand": "Materials and their properties",
    "element": "Practices",
    "year_levels": [1],
    "statements": [
        "Identifying observable properties of materials using the five senses (where appropriate) (e.g. shape, texture, colour, hardness, flexibility)",
        "Identifying the primary material an object is made from (e.g. wood, metal, plastic, glass, fabric, rock)",
        "Comparing and grouping together a variety of everyday materials based on their shared physical properties"
    ]
})

# MATERIALS - Year 2 Practices
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Materials",
    "sub_strand": "Material properties and uses",
    "element": "Practices",
    "year_levels": [2],
    "statements": [
        "Sorting and grouping materials based on how they behave physically, focusing on their mechanical properties, using simple comparisons",
        "Formulating a repeatable method to test how elastic objects behave when stretched or compressed and released, using simple comparisons (e.g. large stretch → larger/faster movement)",
        "Evaluating which materials are best suited for specific uses, based on their observable features"
    ]
})

# MATTER INTERACTIONS AND ENERGY - Year 3 Knowledge - Light and shadow
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Matter Interactions and Energy",
    "sub_strand": "Light and shadow",
    "element": "Knowledge",
    "year_levels": [3],
    "statements": [
        "Light is needed for humans to see objects.",
        "Light travels from a source and can be reflected, scattered, or absorbed.",
        "The Sun is a source of light; the Moon is not (it reflects light from the Sun).",
        "It is dangerous to directly observe the Sun.",
        "Objects appear smaller when they are farther away. This effect is due to visual perspective.",
        "Darkness occurs when there is no light present.",
        "Shadows are formed when light is blocked by an object.",
        "Opaque materials block light (they reflect or absorb it).",
        "Translucent materials let some light through (reflecting, scattering, or absorbing some light).",
        "Transparent materials let all or most light through."
    ]
})

# MATTER INTERACTIONS AND ENERGY - Year 3 Knowledge - Sound
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Matter Interactions and Energy",
    "sub_strand": "Sound",
    "element": "Knowledge",
    "year_levels": [3],
    "statements": [
        "Sound travels as a wave through materials.",
        "Shaking or vibrating materials creates sound.",
        "Sound causes materials to vibrate.",
        "The size of a wave or vibration affects how loud a sound is; larger waves produce louder sounds.",
        "Volume is how loud or quiet a sound is.",
        "The volume of a sound decreases as the distance from its source increases.",
        "Pitch is how high or low a sound is (e.g. a whistle has a high pitch, a drum has a low pitch).",
        "Sound frequency is a measure of how often a sound happens every second. Higher frequency means a higher pitch, and lower frequency means a lower pitch.",
        "How much a material vibrates affects frequency (how high or low the sound is).",
        "Sound frequency is determined by the source and typically remains constant.",
        "Materials can affect the volume and clarity of sound as it travels.",
        "The way sound travels through a material depends on the material's properties, such as its size (length and thickness), how stretchy or hard it is, and how smooth or rough its surface is."
    ]
})

# MATTER INTERACTIONS AND ENERGY - Year 3 Practices - Light and shadow
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Matter Interactions and Energy",
    "sub_strand": "Light and shadow",
    "element": "Practices",
    "year_levels": [3],
    "statements": [
        "Testing and describing how materials interact with light, identifying whether the materials are opaque, translucent, or transparent and whether the light is reflected, scattered, or absorbed",
        "Tracking and measuring how shadows form and change when objects block light",
        "Using diagrams to depict how changes in the position of the light source (such as the Sun at different times of day) influence shadow length and direction"
    ]
})

# MATTER INTERACTIONS AND ENERGY - Year 3 Practices - Sound
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Matter Interactions and Energy",
    "sub_strand": "Sound",
    "element": "Practices",
    "year_levels": [3],
    "statements": [
        "Predicting, comparing, and explaining the relationship between distance and the volume of sound",
        "Carrying out simple tests to observe how sound changes when it travels through different materials and describing how these changes affect the sound (e.g. cup-and-string phone, tapping on a bowl filled with water vs air)",
        "Using simple objects (e.g. elastic bands, string, rulers, slinky) to investigate how sound is produced by vibrating materials",
        "Using musical instruments, including examples from te ao Māori (e.g. conch shell (pūtātara), small flute (kōauau)), to investigate how sounds can cause materials to vibrate and explaining how vibration affects frequency (pitch) and volume"
    ]
})

# MOTION AND FORCES - Year 2 Knowledge
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Motion and Forces",
    "sub_strand": "Motion and changes",
    "element": "Knowledge",
    "year_levels": [2],
    "statements": [
        "Pushes and pulls are interactions between two or more objects and can act in different directions.",
        "Magnets can cause pushes or pulls with some metals or other magnets.",
        "Pushing or pulling an object can cause the object to change direction, speed, or shape.",
        "Objects can move in different ways (e.g. roll, slide, bounce) depending on their shape.",
        "Materials and objects can be changed physically by pushing, pulling, and twisting.",
        "Pushing or pulling something harder can make it move faster.",
        "Different surfaces and shapes can change how fast an object moves."
    ]
})

# MOTION AND FORCES - Year 1 Practices
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Motion and Forces",
    "sub_strand": "Motion and changes",
    "element": "Practices",
    "year_levels": [1],
    "statements": [
        "Investigating how the shape of an object affects whether it rolls, slides, or stays still when pushed or pulled and describing these patterns using simple comparisons",
        "Predicting how objects of different sizes, shapes, or masses move when the same push is applied",
        "Investigating how pushing, pulling, squashing, bending, twisting, or stretching can change the shape or movement of solid objects"
    ]
})

# EARTH AND SPACE - Year 3 Knowledge
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Earth and Space",
    "sub_strand": "The Earth and Sun",
    "element": "Knowledge",
    "year_levels": [3],
    "statements": [
        "The movement of the Earth in relation to the Sun causes observable patterns, including the rising and setting of the Sun, the length of a day, and the length of a year.",
        "The Earth is roughly spherical.",
        "The Earth rotates on its axis once every 24 hours.",
        "The side of Earth facing the Sun experiences daytime, receiving light, and warming through the day. The side facing away from the Sun experiences night-time, and gradually cools through the night.",
        "Shadows change during the day, along with the Sun's position in the sky.",
        "The Earth orbits (revolves around) the sun and takes one year (365 and a quarter days) to complete one full orbit.",
        "A planet is a large object that orbits a star. Planets do not emit light.",
        "A star is a massive ball of hot gases that emits light and other radiation.",
        "The Sun is a star and the Earth is a planet."
    ]
})

# EARTH AND SPACE - Year 3 Practices
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Earth and Space",
    "sub_strand": "The Earth and Sun",
    "element": "Practices",
    "year_levels": [3],
    "statements": [
        "Using models and diagrams to explain how Earth's rotation causes day and night and the apparent movement of the Sun"
    ]
})

# =====================
# BIOLOGICAL SCIENCE
# =====================

# ORGANISM DIVERSITY - Year 1 Knowledge - Discovering life
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Organism Diversity",
    "sub_strand": "Discovering life",
    "element": "Knowledge",
    "year_levels": [1],
    "statements": [
        "All living things are organisms.",
        "There is a wide variety of organisms (this is diversity), including plants, animals, and fungi.",
        "Plants exist in many forms, including grasses, ferns, trees, and seaweeds; they can be flowering or cone-bearing, deciduous or evergreen. Algae such as seaweeds, share some similarities with plants.",
        "Common structures of flowering plants (including trees) include leaves, flowers, fruit, roots, seeds, trunk, branches, and stem.",
        "Ocean plants have different structures to land-based plants.",
        "Animals include diverse groups such as fish, amphibians, reptiles, birds, insects, and mammals (including humans). Each group has distinct features.",
        "Fungi are living organisms that are different from plants and include mushrooms."
    ]
})

# ORGANISM DIVERSITY - Year 2 Knowledge - Life cycles
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Organism Diversity",
    "sub_strand": "Life cycles",
    "element": "Knowledge",
    "year_levels": [2],
    "statements": [
        "Animals, including humans, reproduce and grow into adults.",
        "Offspring often resemble their parents but are not exactly the same as them.",
        "Organisms eventually die.",
        "Different organisms have different life cycles (e.g. butterfly, frog, human, broad bean, kōwhai tree).",
        "Plants grow from seeds, mature, and reproduce.",
        "Flowers are primarily for reproduction.",
        "Flowers play an important role in the life cycle of flowering plants: pollination, seed formation, and seed dispersal.",
        "A seed contains stored nutrients and needs water to germinate."
    ]
})

# ORGANISM DIVERSITY - Year 3 Knowledge - How organisms meet their needs
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Organism Diversity",
    "sub_strand": "How organisms meet their needs",
    "element": "Knowledge",
    "year_levels": [3],
    "statements": [
        "In plants, each structure has a function (e.g. roots and stems help support the plant and transport water and nutrients).",
        "Plants gain nutrition by absorbing sunlight in their leaves to produce sugar (this is photosynthesis); they take up water and nutrients from the soil through their roots.",
        "Animals gain nutrition by digesting other organisms.",
        "Different types of animals have varied diets, with some eating plants (herbivores), some eating other animals (carnivores), and some eating a variety of foods (omnivores).",
        "Animals have body structures adapted for their diets (e.g. teeth, jaw size, snout/beak length, tongue shape).",
        "The teeth of carnivores and herbivores look different, related to their different functions."
    ]
})

# ORGANISM DIVERSITY - Year 1 Practices - Discovering life
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Organism Diversity",
    "sub_strand": "Discovering life",
    "element": "Practices",
    "year_levels": [1],
    "statements": [
        "Classifying both familiar and unfamiliar organisms as plants, animals, or fungi using observable features (e.g. tūtae kēhua is a basket fungi)",
        "Using observable physical features to distinguish different organisms (e.g. kōwhai, kererū, mushroom)",
        "Classifying organisms into broad groups based on shared characteristics (e.g. flax, northern rātā and pōhutukawa)",
        "Identifying and naming a selection of local plants and animals using both English and te reo Māori"
    ]
})

# ORGANISM DIVERSITY - Year 2 Practices - Life cycles
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Organism Diversity",
    "sub_strand": "Life cycles",
    "element": "Practices",
    "year_levels": [2],
    "statements": [
        "Identifying physical features that indicate relatedness between individuals and recognising variation of these features within and across related individuals or groups (e.g. parent/offspring, mammals, birds)",
        "Comparing simple aspects of life cycles in different animals, including life span and changes from young to adult (e.g. egg to caterpillar to butterfly, egg to chick to bird, tadpole to frog)",
        "Observing and interpreting visible transformations in organisms as part of their life cycle (e.g. caterpillars transforming into butterflies, buds opening into flowers)",
        "Using observation and representations such as diagrams to explain how flowering plants reproduce through pollination, seed formation, and dispersal"
    ]
})

# ORGANISM DIVERSITY - Year 3 Practices - How organisms meet their needs
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Organism Diversity",
    "sub_strand": "How organisms meet their needs",
    "element": "Practices",
    "year_levels": [3],
    "statements": [
        "Comparing the functions of plant structures to explain how each contributes to growth, survival, or reproduction",
        "Carrying out basic tests on how environmental factors (e.g. light, water) affect plant growth",
        "Comparing the diets of different types of animals (herbivores, carnivores, omnivores) and explaining how their body structures (e.g. teeth, jaw size, snout/beak length, tongue shape) relate to the food types they consume",
        "Predicting the type of diet an animal eats based on the size and shape of its teeth"
    ]
})

# BODY SYSTEMS - Year 1 Knowledge - Body basics
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Body Systems",
    "sub_strand": "Body basics",
    "element": "Knowledge",
    "year_levels": [1],
    "statements": [
        "The human body consists of major parts such as the head, neck, torso, arms (including elbows), legs (including knees), face, ears, eyes, nose, hair, mouth, and teeth.",
        "Different body parts are associated with senses, including sight, hearing, touch, taste, and smell."
    ]
})

# BODY SYSTEMS - Year 2 Knowledge - What organisms need to survive
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Body Systems",
    "sub_strand": "What organisms need to survive",
    "element": "Knowledge",
    "year_levels": [2],
    "statements": [
        "Animals and fungi depend on other organisms for nutrients, whereas plants can produce their own nutrition.",
        "Plants need water, carbon dioxide (often from the air), light, and space to survive.",
        "Animals need food (nutrition), water, oxygen (often from the air), and space to survive.",
        "Organisms have structural features and behaviours that help them to survive where they live. These are called adaptations.",
        "Animals have body parts for sensing, movement, protection, and resource gathering (e.g. kiwi have long, sensitive beaks for finding insects and worms in forest leaf litter and soil).",
        "Organisms sense stimuli (e.g. light, heat, contact) in their environment and respond to them."
    ]
})

# BODY SYSTEMS - Year 3 Knowledge - Support and movement
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Body Systems",
    "sub_strand": "Support and movement",
    "element": "Knowledge",
    "year_levels": [3],
    "statements": [
        "Humans and some other animals have internal skeletons (including spine, ribcage, and skull) and muscles for support, protection, and movement. These are called the skeletal and muscular systems. These systems work together.",
        "Some animals have external skeletons (e.g. exoskeletons in insects like the wētā and in spiders, shells on molluscs).",
        "Some animals have no skeleton (e.g. slugs) and some also have no muscles (e.g. jellyfish).",
        "Animals with an internal skeleton are called vertebrates. Animals without an internal skeleton are called invertebrates. Most animals are invertebrates.",
        "Some plants have a structural support system (e.g. trunk, branch, stem). Woody plants (e.g. trees) can grow taller than non-woody plants (e.g. grass, ponga)."
    ]
})

# BODY SYSTEMS - Year 1 Practices - Body basics
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Body Systems",
    "sub_strand": "Body basics",
    "element": "Practices",
    "year_levels": [1],
    "statements": [
        "Linking the shape and position of body parts to their function, including how the major sense organs help us explore our world (e.g. fingertips help us feel things like smooth, rough, hot, or cold)"
    ]
})

# BODY SYSTEMS - Year 2 Practices - What organisms need to survive
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Body Systems",
    "sub_strand": "What organisms need to survive",
    "element": "Practices",
    "year_levels": [2],
    "statements": [
        "Identifying and describing the functions of external body parts in animals and external parts in plants using real-life examples",
        "Investigating adaptations of organisms in different environments",
        "Identifying and explaining responses to stimuli in plants and animals (e.g. seedlings growing towards light, wētā hiding when touched, goosebumps forming on skin in cold weather) using observations and simple cause-and-effect reasoning"
    ]
})

# BODY SYSTEMS - Year 3 Practices - Support and movement
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Body Systems",
    "sub_strand": "Support and movement",
    "element": "Practices",
    "year_levels": [3],
    "statements": [
        "Applying simple movement analysis techniques, such as observing and recording their own or others' movements, to understand how muscles create motion",
        "Investigating how muscles and bones interact during specific physical activities and identifying ways body structures provide protection and support in real-life scenarios",
        "Classifying plants based on their structural support system (e.g. trees have a woody trunk)",
        "Observing and classifying animals as invertebrate or vertebrate"
    ]
})

# ECOSYSTEMS - Year 1 Knowledge - Where and how organisms live
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Ecosystems",
    "sub_strand": "Where and how organisms live",
    "element": "Knowledge",
    "year_levels": [1],
    "statements": [
        "Organisms are found in almost every place on Earth.",
        "Some organisms are active during the day, others at night (nocturnal).",
        "Some organisms live alone (e.g. tree), and others live in groups (e.g. hive of bees)."
    ]
})

# ECOSYSTEMS - Year 2 Knowledge - Habitats
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Ecosystems",
    "sub_strand": "Habitats",
    "element": "Knowledge",
    "year_levels": [2],
    "statements": [
        "Habitats are places where organisms interact with other organisms and can find the resources they need for survival (e.g. Maui dolphins live in coastal waters where they can catch small fish).",
        "Communities are groups of organisms that live and interact in the same place.",
        "Animals and plants vary across habitats (e.g. beach, ocean, rainforest).",
        "A habitat supports a variety of organisms.",
        "A microhabitat is a small habitat (e.g. under stones or leaf litter)."
    ]
})

# ECOSYSTEMS - Year 3 Knowledge - Food chains
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Ecosystems",
    "sub_strand": "Food chains",
    "element": "Knowledge",
    "year_levels": [3],
    "statements": [
        "Nutrition is transferred from one organism to another when organisms eat other organisms.",
        "Plants produce their own nutrition and form the beginning of a food chain, followed by herbivores, omnivores, and carnivores."
    ]
})

# ECOSYSTEMS - Year 1 Practices - Where and how organisms live
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Ecosystems",
    "sub_strand": "Where and how organisms live",
    "element": "Practices",
    "year_levels": [1],
    "statements": [
        "Observing and describing how organisms interact with their surroundings (e.g. tūī flying between trees, wētā crawling under logs, sea stars clinging to rocks)",
        "Recognising and comparing behavioural rhythms in organisms related to time of day (e.g. morepork active at night, butterfly flying during the day)",
        "Identifying and describing social behaviours in organisms by comparing solitary and group living patterns (e.g. kākāpō foraging alone, honeybees living in hives)"
    ]
})

# ECOSYSTEMS - Year 2 Practices - Habitats
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Ecosystems",
    "sub_strand": "Habitats",
    "element": "Practices",
    "year_levels": [2],
    "statements": [
        "Recognising and describing features of communities, habitats, and microhabitats (e.g. leaf litter, rock pools) through observation and data",
        "Using cause-and-effect language to explain how survival links to environment resources (e.g. kiwi eat forest floor insects, kina need to be in water)",
        "Identifying and explaining how the structural features and behaviours of organisms support their survival in their habitats (e.g. pāua have a large, muscular foot to stick to rocks)"
    ]
})

# ECOSYSTEMS - Year 3 Practices - Food chains
statements.append({
    "curriculum_version": "draft_2025",
    "version_status": "consultation",
    "learning_area": "Science",
    "phase": "Phase 1",
    "strand": "Ecosystems",
    "sub_strand": "Food chains",
    "element": "Practices",
    "year_levels": [3],
    "statements": [
        "Identifying simple nutritional relationships between animals and plants using basic food chains"
    ]
})

# Print summary
print(f"\n=== SCIENCE PHASE 1 EXTRACTION SUMMARY ===")
print(f"Total statement groups: {len(statements)}")

total_statements = sum(len(group["statements"]) for group in statements)
print(f"Total individual statements: {total_statements}")

print("\n=== BREAKDOWN ===")
for group in statements:
    print(f"{group['strand']} | {group['sub_strand']} | {group['element']} | Year {group['year_levels'][0]}: {len(group['statements'])} statements")

print("\n✅ Ready to insert via MCP Supabase tool!")
print("Execute: mcp_supabase_execute_sql with INSERT statements")

