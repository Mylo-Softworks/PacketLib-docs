Usage
#####

.. note::
    For information about protocols, see :ref:`transmitters`.

.. warning::
    Both client and server need to be polled regularly. Packets are processed during `Poll()` calls.


Starting a server
*****************

.. tabs::
    .. code-tab:: csharp

        using PacketLib.Base; // Client and server classes
        using PacketLib.Transmitters; // Default transmitters

        var server = new NetworkServer<TcpTransmitter>(reg); // Creates a tcp server


Starting a client
*****************

.. tabs::
    .. code-tab:: csharp

        using PacketLib.Base; // Client and server classes
        using PacketLib.Transmitters; // Default transmitters

        var server = new NetworkClient<TcpTransmitter>(reg); // Creates a tcp client


Polling
*******

.. note::
    Polling must be called regularly for as long as the server/client exists.

Polling the server.

.. tabs::
    .. code-tab:: csharp

        server.Poll();

Polling the client.

.. tabs::
    .. code-tab:: csharp
    
        client.Poll();


Sending packets
***************

Client to server
================

.. tabs::
    .. code-tab:: csharp
    
        client.Send(packet);


Server to client
================

With client Guid

.. tabs::
    .. code-tab:: csharp

        server.SendToClient(packet, Guid);

With ClientRef object

.. tabs::
    .. code-tab:: csharp

        clientRef.Send(packet);


Server to all clients
=====================

.. tabs::
    .. code-tab:: csharp
    
        server.SendToAll(packet);


Events
******

Client connected
================

From server side.

.. tabs::
    .. code-tab:: csharp
    
        server.ClientConnected += (sender, @ref) =>
        {
            Console.WriteLine($"[Server] Client connected: {@ref.Guid}!");
        };

From client side.

.. tabs::
    .. code-tab:: csharp

        client.ClientConnected += (sender, guid) =>
        {
            Console.WriteLine($"[Client] Client connected! {guid}");
        };


Client disconnected
===================

From server side.

.. tabs::
    .. code-tab:: csharp
    
        server.ClientDisconnected += (sender, @ref) =>
        {
            Console.WriteLine($"[Server] Client disconnected! {@ref.Guid}!");
        };

From client side.

.. tabs::
    .. code-tab:: csharp

        client.ClientDisconnected += (sender, _) =>
        {
            Console.WriteLine($"[Client] Client disconnected!");
        };
