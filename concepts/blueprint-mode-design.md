# Blueprint Mode Design - Primary Source

**Date:** 2026-01-29
**Type:** Design concept (unedited)

---

I think command queue is the closest, with an element of action point regeneration. So, you wait until the characters you want to move are ready to move (AP) then say you have 3 characters with filled move bars. Now you can enter a blueprint mode (like a shulk xenoblade see the future, or the mila's divine protection, time turner rewind) and it's basically a debug menu where you can apply a movement actions within your constraints. So unlike any of those other games, you have parallelism here if you're willing to wait for multiple AP meters to fill up, or if the (earlier I said debug menu) or if the you need an immediate action, then you can bring up this blueprint mode, assort your actions along a timeline (AP consumption of the whole bar, but can only act when the bar is at 100%, so you accept faster refills but a shorter string length of actions, even on characters that are slower to refill their AP.

Really now that I explain it, it very much is like the ink mechanic in splatoon, but kind of upside down. In splatoon you consume ink and can only do actions while the ink is refilled, whereas in this game, you can only do actions when your AP is 100% and the actions you do diverge you from your next refilled 100% bar.

The idea is that this enables a method of member method of sections analysis to team play, because you have true parallelism and coordination in a fire emblem setting. And then, it's micro armies, because an enemy side might have their AP filled and they can set up their parallel actions to be done. You can have some unique expressions of coordinated mob enemies. For example, like ravens in a forest that dive at the player, or land based enemies like the "moblins" from zelda windwaker that mob the player. They appear in numbers and their strength is in numbers. They make constraint shapes as part of their AI, so limit player movements and actions, and escort others of them who are focused on moving around and dealing damage.

AOE damage would be especially useful here because the problem of dealing with these enemies is so tactically slow to pick apart one by one (where they have full autonomy), then AOE picks apart the group by sections. Player strategy gets more interesting now because coordination is the new game, instead of encouraging turtling like fire emblem games typically do, if you turtle, there aren't enough spaces for your units to pass through. You need arteries in the design of your coordination. That design is up for the player to learn, and the game assists / challenges the player.

I do have a system in mind to make replication of coordinations more accessible to players that want to generate their own strategy templates/patterns. It starts becoming a bit like the auto-build mechanic in tears of the kingdom. A somewhat experienced player that likes approaching strategies in a consistent way can register a template of that strategy for easy access in blueprint mode. The number of templates/snippets that you can register is limited, with the possibility of upgrading the number still being considered. Both the number of these snippets you can have registered at once and the complexity of control and the number of units that are registered to participate in this snippet are the three ways that I envision the possibility of upgrading this.

Now the users have parallelism enabled by this RTS-like system, and they eventually unlock access to a system that crystallizes their preferred patterns, with complexity of their snippets/patterns/templates being tied to game progression. Both players and enemies utilize this mechanic. Progression on this metric I think would feel critical but ultimately optional. These snippets are a quality of life feature because as levels get more involved, I wouldn't want the user to get stuck in blueprint mode. The user should feel like blueprint mode is their thinking environment and the controls in it are critical to a smooth pace between creating an action plan and seeing those steps play out in the level context.

Of course, all of this would need associated testing. For example, basics are opening and closing blueprint mode (or whatever the name will be for the end user, blueprint mode is an internal name), then in blueprint mode, selecting a micro fundamental action, and letting the action play out would be another test. And then, if you have an interface for fundamental actions, then you can write one test using the interface and an array with instances of each fundamental action being saved as objects in the elements of this array (array[interface]; test on interface)

I think, my design will prioritize for now making enemies and maps that are representative of broad behaviors. For example, the ravens AI would be good to create. Then that AI (I don't know) might be foundational to folk in a town cafe coordinating their walking, if the player goes shopping. Same for maps. A standard block with constraint JSON might start as a block of grass, but might become a basket, or a falling apple or a sand monster with collision/knockback making plays in the parallel attack setting to disrupt the player's action plans. Contiguous. Pretty much, we start with identities that seem to capture a lot of useful behaviors, then when we plan next, we work with what we have.

By the way, combine parallelism with 3D movement and any character specific skills like the rainbow unicorn creating a sky trail or falcons flying in dogfighting trajectories that we prebuilt for the player to use (and interrupt) as they please in their action plans would make for what I think is a fun game.

---

**Related Documents:**
- `blueprint-mode-interpretation.md` - Claude's interpretation and action items
- `constraint-interface-pattern.md` - Constraint system design
