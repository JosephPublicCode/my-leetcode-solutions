-- leetcode 610

-- Triangle Judgement

-- Sum of any two sides must exceed the third side

SELECT x, y, z, IF((x + y) > z,
                    IF((x + z) > y,
                        IF((y + z) > x,
                        "Yes",
                        "No"),
                        "No"),
                        "No") 
                        as triangle
FROM Triangle




SELECT x, y, z, IF((x + y) > z and (x + z) > y and (y + z) > x, "Yes", "No") as triangle
FROM Triangle