Packets
#######

Packets are classes which contain a payload which can be transmitted over the internet.

.. important::
    The packet's payload must be serializable with `SerializeLib <https://serializelib.readthedocs.io/latest/>`_.


The payload can be accessed through the `Payload` field.

Creating packets
****************

With an empty payload
=====================

.. tabs::
    .. code-tab:: csharp

        using PacketLib.Packet;

        public class ExamplePacket : Packet<EmptyPayload>
        {

        }


With a serializable payload
===========================

.. tabs::
    .. code-tab:: csharp

        using PacketLib.Packet;

        public class ExamplePacket : Packet<long>
        {

        }


Creating custom payloads
************************

Any serializable object can be used as a payload, so for a payload with a bool and an int, this would be the code.

.. tabs::
    .. code-tab:: csharp

        using SerializeLib.Attributes;

        [SerializeClass]
        public class ExamplePayload
        {
            [SerializeField] public int ExampleInt;
            [SerializeField] public bool ExampleBool;
        }


Adding functionality to packets
*******************************

There are two functions for processing packets, one for the client, one for the server.

.. tabs::
    .. code-tab:: csharp

        public override void ProcessClient<T>(NetworkClient<T> client)

Processes a packet on the client. The NetworkClient is passed as the `client` argument.

.. tabs::
    .. code-tab:: csharp
    
        public override void ProcessServer<T>(NetworkServer<T> server, ClientRef<T> source)

Processes a packet on the server. The `NetworkServer` is passed as the `server` argument, and the `ClientRef` the packet was received from is passed as the `source` argument.