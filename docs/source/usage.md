# Usage

```{note}
For information about protocols, see [transmitters](transmitters).
```
```{warning}
Both client and server need to be polled regularly. Packets are processed during `Poll()` calls.
```

## Starting a server
```csharp
using PacketLib.Base; // Client and server classes
using PacketLib.Transmitters; // Default transmitters

var server = new NetworkServer<TcpTransmitter>(reg); // Creates a tcp server
```

## Starting a client
```csharp
using PacketLib.Base; // Client and server classes
using PacketLib.Transmitters; // Default transmitters

var server = new NetworkClient<TcpTransmitter>(reg); // Creates a tcp client
```

## Polling
```{note}
Polling must be called regularly for as long as the server/client exists.
```
Polling the server.
```csharp
server.Poll();
```
Polling the client.
```csharp
client.Poll();
```

## Sending packets
### Client to server
```csharp
client.Send(packet);
```

### Server to client
With client Guid
```csharp
server.SendToClient(packet, Guid);
```
With ClientRef object
```csharp
clientRef.Send(packet);
```

### Server to all clients
```csharp
server.SendToAll(packet);
```

## Events
### Client connected
From server side.
```csharp
server.ClientConnected += (sender, @ref) =>
{
    Console.WriteLine($"[Server] Client connected: {@ref.Guid}!");
};
```
From client side.
```csharp
client.ClientConnected += (sender, guid) =>
{
    Console.WriteLine($"[Client] Client connected! {guid}");
};
```

### Client disconnected
From server side.
```csharp
server.ClientDisconnected += (sender, @ref) =>
{
    Console.WriteLine($"[Server] Client disconnected! {@ref.Guid}!");
};
```
From client side.
```csharp
client.ClientDisconnected += (sender, _) =>
{
    Console.WriteLine($"[Client] Client disconnected!");
};
```