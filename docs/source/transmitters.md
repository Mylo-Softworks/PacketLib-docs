# Transmitters

Transmitters are implementations of protocols, used for sending data between client and server.

Transmitters are of type `TransmitterBase<Self>`.

## Built in transmitters
* `TcpTransmitter`
* `UdpTransmitter`

## Writing custom transmitters
To write a custom transmitter, you must inherit the `TransmitterBase<Self>` class.

### TransmitterBase class
```csharp
public class ExampleProtocol : TransmitterBase<ExampleProtocol>
{
    // Errors because abstract methods need to be implemented.
}
```

### Abstract methods explained
```csharp
protected override void InitClientRefImpl(object transfer)
```
Called when a transmitter is a remote client.  
`transfer` is used to initialize the needed values, you will be calling `InitClientRef` when you detect a new client, and passing this into `OnNewServerConnection`.

```csharp
protected override void ConnectImpl(IPEndPoint host)
```
Called when a transmitter is a local client.  
You should connect to the specified `host` endpoint if this is called.

```csharp
protected override void HostImpl(IPEndPoint host)
```
Called when a transmitter is a host.  
You should start listening on the `host` endpoint if this is called.

```csharp
protected override void DisconnectImpl()
```
Implementation of disconnecting.  
Most transmitters should just call dispose here, as a transmitter is linked to a connection, so when the connection is closed, or a disconnect is indicated by packet; the transmitter is no longer valid..

```csharp
protected override void SendImpl(Action<Stream> streamWrite)
```
Implementation of sending data.  
`streamWrite` can be called with a stream as the parameter to write to this stream, the packet's data will be written.

```csharp
protected override List<dynamic>? PollImpl()
```
Implementation of polling.   
This method will be called very frequently, when it is called, 
the transmitter should return the result of `PacketRegistry.ReadPacketDataUntilThisPoint(stream)`. 
The stream will be read, and the data will be deserialized into packets.  
`PacketRegistry` holds a buffer which will keep track of the last incomplete packet in the stream. 
This is used primarily for parsing TcpClient streams effectively.

```csharp
public override bool IsConnected()
```
Return true if the client is connected or the protocol is connectionless. Return false if not (yet) connected.

```csharp
public override bool IsConnecting()
```
Return true if the client is connecting but not yet connected. Return false if not connected, already connected, or protocol is connectionless.

```csharp
public override bool ShouldQueueRemoveImpl()
```
Return true if the transmitter should be removed if it's still connected to a server. Otherwise return false.

```csharp
public override void Dispose()
```
Method used to free resources associated with this object. (From IDisposable)
