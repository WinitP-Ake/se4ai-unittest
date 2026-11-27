# Reflection

Name: Winit Pongsripian

Answer each question in 1–2 sentences.

**1. How many bugs did your tests catch in your first bug hunt, and how many at the end?**

> My tests caught 9 of 11 bugs on the first bug hunt, missing bug08 and bug09. After adding targeted tests for those two cases, my suite caught all 11 of 11 bugs.

**2. Pick one bug your first tests missed. What kind of input did you not think of, and which test did you add to catch it?**

> For bug09, I did not think to test inequality between two fractions that share the same numerator but have different denominators, such as Rational(1, 2) and Rational(1, 3). I added a test asserting Rational(1, 2) != Rational(1, 3) to catch any equality check that ignores denominators.
