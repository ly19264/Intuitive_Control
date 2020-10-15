using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Way_Check_Result : MonoBehaviour
{
    // Start is called before the first frame update
    public int[] waypoint_ids;

    public Material Success;

    public Material Fail;

    public int[] way_results;

    private int way_count;

    // Update is called once per frame
    void Update()
    {

        if (RosSharp.RosBridgeClient.Pose_Array_Send.publish_flag == 1)
        {

            way_count = RosSharp.RosBridgeClient.Pose_Array_Send.waypoint_array.Length;
            way_results = new int[way_count];

            way_results = RosSharp.RosBridgeClient.Way_Check.way_result;
            for (int i = 0; i < way_count; i++)
            {
                if (way_results[i] == 1)
                {
                    RosSharp.RosBridgeClient.Pose_Array_Send.waypoint_array[i].GetComponent<MeshRenderer>().material = Fail;
                }
                if (way_results[i] == 2)
                {
                    RosSharp.RosBridgeClient.Pose_Array_Send.waypoint_array[i].GetComponent<MeshRenderer>().material = Success;
                }
            }
        }
    }
}
