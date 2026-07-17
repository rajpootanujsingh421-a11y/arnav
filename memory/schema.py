class MemorySchema:
    
    ALLOWED_KEYS = {
        "name",
        "age",
        "city",
        "country",

        "college",
        "degree",
        "branch",
        "semester",

        "favorite_language",
        "favorite_music",
        "favorite_food",

        "goal",
        "dream",

        "project",
        "hobby",

        "profession"
        
        "likes",
        "dislikes",

        "favorite_editor",

        "os",

        "github",

        "skills",

        "routine",

        "workout",

        "current_project"
    }

    @classmethod
    def is_valid(cls, key: str) -> bool:
        return key in cls.ALLOWED_KEYS