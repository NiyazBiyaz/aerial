# Aerial
New perspective on AI

## About

Aerial based on modularity and interpretability principles.
Also, it must be able to run on your PC!

#### Aerial have 3 base parts:
- Core
- Memory
- Handlers

Core provides a reasoning chains: search, plan, solve. It's a center of all system. Uses Handlers for the interact with everything.

Memory provides the core with knowledge so that it does not rely on its own weights, but takes them from the database.

Handlers it's a external modules of Aerial, that accepts requests from Core and works with this. Their capabilities based on Protocol. 

## Terms

### **Protocol**

#### *Summary*:
Definitions of rules about interaction between different modules of the Aerial. 

This explains how different modules of the system should interact with each other. **Core** is a key component of Aerial, so the protocol mainly specifies what capabilities it should have and what capabilities Handlers should provide.

#### *Versions*
Different protocol versions also provides smooth growth of the all system on each development step. Every module is based on protocol, and their behaviour should be relevant of defined in it. 
