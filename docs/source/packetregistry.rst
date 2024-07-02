PacketRegistry
##############

The `PacketRegistry` class is used to register packets for lookup.

Registering packets
*******************

Automatic
=========

You can register an entire assembly automatically using `RegisterAssembly()`.

.. tabs::
    .. code-tab:: csharp

        using PacketLib.Packet;

        var reg = new PacketRegistry();
        reg.RegisterAssembly(Assembly.GetExecutingAssembly());

Manual
======
You can register individual packets using `RegisterPacket()`.

.. tabs::
    .. code-tab:: csharp

        using PacketLib.Packet;

        var reg = new PacketRegistry();
        reg.RegisterPacket(typeof(ExamplePacket));

Force register
==============
You can register a packet at a specific ID using `ForceRegisterPacket()`.

.. tabs::
    .. code-tab:: csharp

        using PacketLib.Packet;

        var reg = new PacketRegistry();
        reg.ForceRegisterPacket(typeof(ExamplePacket), (ushort)10); // Registers the packet at index 10
