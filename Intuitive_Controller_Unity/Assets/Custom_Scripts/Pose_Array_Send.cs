using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Security.Cryptography;
using UnityEngine;
using Valve.VR;

namespace RosSharp.RosBridgeClient
{
    public class Pose_Array_Send : UnityPublisher<MessageTypes.Geometry.PoseArray>
    {
        public string FrameId = "Unity";

        private MessageTypes.Geometry.PoseArray message;

        private MessageTypes.Geometry.Pose local_pose;

        public SteamVR_Action_Boolean trigger_clicked;

        public SteamVR_Action_Boolean publish_clicked;


        public Transform waypoint_plotter_tracker;

        private Vector3 waypoint_position;

        public GameObject waypoint_prefab;
        
        private GameObject onplay_waypoint;

        public static GameObject[] waypoint_array;

        public static int publish_flag;


        private int click_count;




        protected override void Start()
        {
            click_count = 0;
            publish_flag = 0;
            base.Start();
            InitializeMessage();
        }

        private void FixedUpdate()
        {
            UpdateMessage();
        }

        private void InitializeMessage()
        {
            message = new MessageTypes.Geometry.PoseArray
            {
                header = new MessageTypes.Std.Header()
                {
                    frame_id = FrameId
                }
            };
            local_pose = new MessageTypes.Geometry.Pose();
            message.poses = new MessageTypes.Geometry.Pose[50];
            waypoint_array = new GameObject[50];
        }

        private void UpdateMessage()
        {
            if (trigger_clicked.GetStateUp(SteamVR_Input_Sources.Any))
            {
                waypoint_position = waypoint_plotter_tracker.position;    //Tracking the hand controller
                onplay_waypoint = Instantiate(waypoint_prefab, waypoint_position, Quaternion.identity);   //Instantiate waypoints in the field of view
                waypoint_array[click_count] = onplay_waypoint;
                
                //Conversion of the coordinates to be sent to the ros
                /*local_pose.position.x = onplay_waypoint.transform.position.z - 3;
                local_pose.position.y = -onplay_waypoint.transform.position.x;
                local_pose.position.z = onplay_waypoint.transform.position.y;

                message.poses[click_count] = local_pose;    //storing the pose in the pose array

                local_pose = new MessageTypes.Geometry.Pose(); //Clear the local pose  */
                click_count = click_count + 1;
            }

            if (publish_clicked.GetStateUp(SteamVR_Input_Sources.Any))
            {
                Array.Resize(ref waypoint_array, click_count);
                message.poses = new MessageTypes.Geometry.Pose[click_count];
                for (int i = 0; i < click_count; i++)
                {
                    //Conversion of the coordinates to be sent to the ros
                    local_pose.position.x = waypoint_array[i].transform.position.z - 3;
                    local_pose.position.y = -waypoint_array[i].transform.position.x;
                    local_pose.position.z = waypoint_array[i].transform.position.y;
                    message.poses[i] = local_pose;
                    local_pose = new MessageTypes.Geometry.Pose();
                }
                publish_flag = 1;
                //Array.Resize(ref message.poses, click_count + 1);
            }
            if (publish_flag == 1)
            {
                Publish(message);
            }                
         }

    }
}