-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- Create Patients Table
create table public.patients (
  id uuid primary key default uuid_generate_v4(),
  first_name text not null,
  last_name text not null,
  phone_number text not null,
  timezone text not null,
  caretaker_id uuid, -- Optional, can link to an auth.users id later
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Create Medications Table
create table public.medications (
  id uuid primary key default uuid_generate_v4(),
  patient_id uuid references public.patients(id) on delete cascade not null,
  name text not null,
  dosage text not null,
  time_to_take text not null, -- Stored as 'HH:MM:SS'
  is_active boolean default true not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);
